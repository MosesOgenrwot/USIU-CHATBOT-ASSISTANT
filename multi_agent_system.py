"""
Multi-Agent System for USIU-Africa Student Support
Specialized agents for different query types
"""

import json
import os
from typing import Dict, List, Any

class QueryRouterAgent:
    """Routes queries to appropriate knowledge domains"""
    
    CATEGORIES = {
        "fees_financial": ["fee", "cost", "tuition", "payment", "pay", "bank", "mpesa", "price", "charge"],
        "academic": ["program", "course", "degree", "major", "gpa", "grade", "credit", "graduation", "admission"],
        "facilities": ["library", "lab", "classroom", "building", "cafeteria", "gym", "hostel", "where is"],
        "services": ["counseling", "health", "career", "financial aid", "scholarship", "housing"],
        "conduct": ["rule", "policy", "conduct", "discipline", "violation", "alcohol", "drug"],
        "general": []
    }
    
    def route(self, query: str) -> str:
        """Determine query category"""
        query_lower = query.lower()
        
        scores = {}
        for category, keywords in self.CATEGORIES.items():
            score = sum(1 for keyword in keywords if keyword in query_lower)
            if score > 0:
                scores[category] = score
        
        if scores:
            return max(scores, key=scores.get)
        return "general"


class KnowledgeRetrieverAgent:
    """Retrieves relevant information from JSON knowledge base"""
    
    def __init__(self, knowledge_dir: str = "knowledge"):
        self.knowledge_dir = knowledge_dir
        self.cache = {}
        self._load_knowledge()
    
    def _load_knowledge(self):
        """Load all JSON files into memory"""
        json_files = [
            "academic_policies_procedures.json",
            "all_programs_fees_2025_2026.json",
            "campus_facilities_services.json",
            "fees_financial_info.json",
            "mastercard_foundation_scholars.json",
            "programs.json",
            "student_conduct_discipline.json",
            "student_services_policies.json"
        ]
        
        for filename in json_files:
            filepath = os.path.join(self.knowledge_dir, filename)
            if os.path.exists(filepath):
                try:
                    with open(filepath, 'r') as f:
                        self.cache[filename] = json.load(f)
                except Exception as e:
                    print(f"Error loading {filename}: {e}")
    
    def retrieve(self, category: str, query: str) -> Dict[str, Any]:
        """Retrieve relevant knowledge based on category"""
        
        # Map categories to knowledge files
        file_mapping = {
            "fees_financial": ["all_programs_fees_2025_2026.json", "fees_financial_info.json"],
            "academic": ["academic_policies_procedures.json", "programs.json"],
            "facilities": ["campus_facilities_services.json"],
            "services": ["student_services_policies.json", "mastercard_foundation_scholars.json"],
            "conduct": ["student_conduct_discipline.json"],
            "general": list(self.cache.keys())
        }
        
        relevant_files = file_mapping.get(category, list(self.cache.keys()))
        
        results = {}
        for filename in relevant_files:
            if filename in self.cache:
                results[filename] = self.cache[filename]
        
        return results


class ResponseGeneratorAgent:
    """Generates natural language responses from retrieved knowledge"""
    
    def __init__(self, llm_provider: str = "groq"):
        self.llm_provider = llm_provider
    
    def generate(self, query: str, knowledge: Dict[str, Any], category: str) -> str:
        """Generate response from knowledge"""
        
        # Simple rule-based response for reliable operation
        if not knowledge:
            return self._generate_fallback(query)
        
        # Extract relevant information based on category
        if category == "fees_financial":
            return self._generate_fees_response(query, knowledge)
        elif category == "academic":
            return self._generate_academic_response(query, knowledge)
        elif category == "facilities":
            return self._generate_facilities_response(query, knowledge)
        elif category == "services":
            return self._generate_services_response(query, knowledge)
        elif category == "conduct":
            return self._generate_conduct_response(query, knowledge)
        else:
            return self._generate_general_response(query, knowledge)
    
    def _generate_fees_response(self, query: str, knowledge: Dict) -> str:
        """Generate response for fees/financial queries"""
        query_lower = query.lower()
        
        # Check for specific program queries
        programs_to_check = {
            "nursing": "Bachelor of Science in Nursing",
            "ai": "Artificial Intelligence (AI) & Robotics", 
            "robotics": "Artificial Intelligence (AI) & Robotics",
            "mba": "Master of Business Administration",
            "psychology": "Bachelor of Arts in Psychology"
        }
        
        for key, program in programs_to_check.items():
            if key in query_lower:
                # Search in fees data
                for file_key, data in knowledge.items():
                    if "programs_fees" in file_key or "fees_financial" in file_key:
                        return self._extract_program_fees(program, data)
        
        # Payment methods query
        if "pay" in query_lower or "payment" in query_lower or "bank" in query_lower:
            return self._extract_payment_info(knowledge)
        
        # M-Pesa query
        if "mpesa" in query_lower or "m-pesa" in query_lower:
            return self._extract_mpesa_info(knowledge)
        
        return "I can help you with information about tuition fees, payment methods, and financial services at USIU-Africa. Please specify which program or service you're interested in."
    
    def _extract_program_fees(self, program: str, data: Dict) -> str:
        """Extract fees for a specific program"""
        # Search through the fee structure
        for category, programs in data.items():
            if isinstance(programs, dict):
                for prog_key, prog_data in programs.items():
                    if isinstance(prog_data, dict):
                        if "program" in prog_data or "programs" in prog_data:
                            program_name = prog_data.get("program") or prog_data.get("programs", [""])[0]
                            if program.lower() in str(program_name).lower():
                                fees = prog_data.get("fees_per_semester", {})
                                if fees:
                                    kenyan = fees.get("kenyan", {}).get("total", "N/A")
                                    ea = fees.get("east_african", {}).get("total", "N/A")
                                    non_ea = fees.get("non_east_african", {}).get("total", "N/A")
                                    
                                    return f"**{program_name} Fees (Per Semester):**\n\n" \
                                           f"- Kenyan Students: KES {kenyan:,}\n" \
                                           f"- East African Students: KES {ea:,}\n" \
                                           f"- Non-East African Students: KES {non_ea:,}\n\n" \
                                           f"Note: Fees include tuition, library, medical, student activity, technology fees, and more."
        
        return f"I couldn't find specific fee information for {program}. Please contact the Finance Office at finance@usiu.ac.ke or call +254 730 116 509."
    
    def _extract_payment_info(self, knowledge: Dict) -> str:
        """Extract payment methods information"""
        for file_key, data in knowledge.items():
            if "fees_financial" in file_key:
                if "payment_methods" in data or "banks" in data:
                    banks_info = data.get("banks", {})
                    if banks_info:
                        response = "**Payment Methods at USIU-Africa:**\n\n"
                        response += "**Bank Deposit Options:**\n"
                        for bank_name, details in banks_info.items():
                            if isinstance(details, dict):
                                response += f"\n• **{bank_name}**\n"
                                if "account_number" in details:
                                    response += f"  Account: {details['account_number']}\n"
                                if "branch" in details:
                                    response += f"  Branch: {details['branch']}\n"
                        
                        response += "\n**M-Pesa:** Business number 516900\n"
                        response += "\n**Note:** No cash payments accepted in Finance Office."
                        return response
        
        return "For payment information, please contact the Finance Office at finance@usiu.ac.ke or +254 730 116 509."
    
    def _extract_mpesa_info(self, knowledge: Dict) -> str:
        """Extract M-Pesa payment information"""
        response = "**M-Pesa Payment Instructions:**\n\n"
        response += "1. Go to M-Pesa\n"
        response += "2. Select 'Lipa na M-Pesa'\n"
        response += "3. Click 'Pay Bill'\n"
        response += "4. Enter Business Number: **516900**\n"
        response += "5. Enter Account Number: **[Your Student ID]-[Purpose Code]**\n"
        response += "   Example: 664XXX-TUIT (for tuition)\n\n"
        response += "**Common Purpose Codes:**\n"
        response += "- TUIT = Tuition/Graduation fees\n"
        response += "- ADM = Application fee\n"
        response += "- LIBF = Library fine\n"
        response += "- TSPT = Transport payment\n"
        response += "- IRF = ID card replacement\n"
        
        return response
    
    def _generate_academic_response(self, query: str, knowledge: Dict) -> str:
        """Generate response for academic queries"""
        query_lower = query.lower()
        
        # GPA requirements
        if "gpa" in query_lower:
            return "**GPA Requirements at USIU-Africa:**\n\n" \
                   "- Undergraduate: Minimum 2.0 GPA\n" \
                   "- Graduate: Minimum 3.0 GPA\n\n" \
                   "Failure to maintain these standards leads to: Warning → Probation → Dismissal\n\n" \
                   "**Honours Graduation:**\n" \
                   "- Cum Laude: 3.50 - 3.69\n" \
                   "- Magna Cum Laude: 3.70 - 3.89\n" \
                   "- Summa Cum Laude: 3.90 - 4.00"
        
        # Programs query
        if "program" in query_lower:
            programs_list = []
            for file_key, data in knowledge.items():
                if "programs.json" in file_key:
                    if "programs" in data:
                        for prog in data["programs"]:
                            programs_list.append(f"- {prog.get('name', 'Unknown')} ({prog.get('total_units', 'N/A')} units)")
            
            if programs_list:
                return "**Available Programs at USIU-Africa:**\n\n" + "\n".join(programs_list[:10]) + \
                       "\n\nFor complete program details, visit www.usiu.ac.ke or contact admissions@usiu.ac.ke"
        
        return "For academic information, please contact the Registrar at Ext 782-790 or the Academic Affairs office."
    
    def _generate_facilities_response(self, query: str, knowledge: Dict) -> str:
        """Generate response for facilities queries"""
        query_lower = query.lower()
        
        # Library hours
        if "library" in query_lower and "hour" in query_lower:
            return "**Library Hours:**\n\n" \
                   "**During Semester:**\n" \
                   "- Monday-Friday: 8:15 AM - 9:00 PM\n" \
                   "- Saturday: 9:00 AM - 6:00 PM\n" \
                   "- Sunday: 11:00 AM - 5:00 PM\n\n" \
                   "**During Vacation:**\n" \
                   "- Monday-Friday: 8:15 AM - 5:00 PM\n" \
                   "- Saturday & Sunday: CLOSED\n\n" \
                   "Contact: Ext 254/294/371 or asklibrarian@usiu.ac.ke"
        
        # Classroom locations
        if "where is" in query_lower or "classroom" in query_lower or "building" in query_lower:
            return "**Campus Buildings & Locations:**\n\n" \
                   "**Chandaria School of Business:** B1-B5, BS1-BS2, LT1-LT2\n" \
                   "**Science Centre:** SC1-SC9, LT3-LT5, Labs A-K\n" \
                   "**Lillian K. Beam Building:** Computer Labs 1-15\n" \
                   "**SHSS:** SS1-SS19, SR1-SR5, LT7-LT8\n" \
                   "**Wooden Blocks:** EF, GH, KL, IJ\n\n" \
                   "For specific locations, check your class schedule or ask at the Administration Block."
        
        # Cafeteria
        if "cafeteria" in query_lower or "meal" in query_lower:
            return "**Cafeteria Hours:**\n\n" \
                   "**Breakfast:** Mon-Sat 7:30-9:30 AM, Sun 9:30 AM-2:00 PM\n" \
                   "**Lunch:** Mon-Sat 12:00-3:00 PM, Sun 12:00-2:00 PM\n" \
                   "**Dinner:** Mon-Sat 7:00-9:30 PM, Sun 6:30-8:30 PM\n\n" \
                   "Contact: Ext 302/208/293"
        
        return "For facilities information, please visit the specific department or call the main office at +254 730 116 290."
    
    def _generate_services_response(self, query: str, knowledge: Dict) -> str:
        """Generate response for services queries"""
        query_lower = query.lower()
        
        # Counseling
        if "counsel" in query_lower:
            return "**Counseling Services:**\n\n" \
                   "Location: Counseling Block (opposite Classrooms I & J)\n" \
                   "Contact: Ext 311/297\n\n" \
                   "**Services:**\n" \
                   "- Personal counseling (confidential)\n" \
                   "- Career counseling\n" \
                   "- Group counseling\n" \
                   "- Life skills development\n" \
                   "- Voluntary Counseling & Testing (VCT)\n\n" \
                   "Walk-in welcome, appointments recommended."
        
        # Health center
        if "health" in query_lower or "medical" in query_lower:
            return "**Health Center:**\n\n" \
                   "Location: Next to Hostels\n" \
                   "Contact: Ext 542/230/229\n\n" \
                   "**Hours:**\n" \
                   "- All students: 8:00 AM - 10:00 PM\n" \
                   "- Resident students (emergency): 10:00 PM - 8:00 AM\n\n" \
                   "**Services:** Clinical diagnosis, prescriptions, minor surgery, vaccinations, health counseling"
        
        # Scholarship
        if "scholarship" in query_lower or "financial aid" in query_lower:
            return "**Financial Aid Programs:**\n\n" \
                   "**Undergraduate:** Full USIU Scholarship, Alumni Scholarship, Sports Scholarship, CWO, RA\n" \
                   "**Graduate:** MBAS Scholarship, Graduate Assistantship\n" \
                   "**All Students:** Special Need Grant, Family Discount, Alumni Discount\n" \
                   "**External:** Mastercard Foundation, HELB, Bank Loans\n\n" \
                   "Contact Financial Aid: finaid@usiu.ac.ke or +254 20 3606210\n\n" \
                   "Note: Application does not guarantee award. Interview required."
        
        return "For student services, contact the Student Affairs office at Ext 436 or visit the Administration Block."
    
    def _generate_conduct_response(self, query: str, knowledge: Dict) -> str:
        """Generate response for conduct/policy queries"""
        query_lower = query.lower()
        
        # Alcohol/drugs
        if "alcohol" in query_lower or "drug" in query_lower or "smoking" in query_lower:
            return "**USIU-Africa Substance Policy:**\n\n" \
                   "**Zero Tolerance Policy:**\n" \
                   "- Campus is alcohol-free and drug-free\n" \
                   "- Smoking/vaping prohibited in all buildings, buses, and compounds\n" \
                   "- Illegal drugs (cannabis, heroin, cocaine, opium): **DISMISSAL**\n" \
                   "- Alcohol violations: **SUSPENSION** (repeat: DISMISSAL)\n" \
                   "- Smoking violations: **Probation Level II** (repeat: SUSPENSION)\n\n" \
                   "Report concerns to Security (Ext 583) or Dean of Students (Ext 187)."
        
        # Sanctions
        if "sanction" in query_lower or "violation" in query_lower or "discipline" in query_lower:
            return "**Disciplinary Sanction Levels:**\n\n" \
                   "1. Warning\n" \
                   "2. Probation Level I\n" \
                   "3. Probation Level II\n" \
                   "4. Interim Suspension\n" \
                   "5. Suspension\n" \
                   "6. Dismissal\n\n" \
                   "**Serious Violations:**\n" \
                   "- Sexual assault/harassment: DISMISSAL\n" \
                   "- Theft/stolen property: DISMISSAL\n" \
                   "- Drugs/illegal substances: DISMISSAL\n" \
                   "- Weapons/firearms: SUSPENSION\n\n" \
                   "Contact Dean of Students (Ext 187) for questions."
        
        return "For conduct and policy questions, refer to the Student Handbook or contact the Dean of Students at Ext 187."
    
    def _generate_general_response(self, query: str, knowledge: Dict) -> str:
        """Generate general response"""
        return "**USIU-Africa Student Support:**\n\n" \
               "I can help you with information about:\n" \
               "- Fees and payments\n" \
               "- Academic programs and policies\n" \
               "- Campus facilities and locations\n" \
               "- Student services and support\n" \
               "- Conduct rules and policies\n\n" \
               "Please ask a specific question, or contact:\n" \
               "- Main Office: +254 730 116 290\n" \
               "- Email: admit@usiu.ac.ke\n" \
               "- Website: www.usiu.ac.ke"
    
    def _generate_fallback(self, query: str) -> str:
        """Generate fallback response when no knowledge is found"""
        return "I apologize, but I don't have specific information about that in my current knowledge base. " \
               "Please contact the appropriate USIU-Africa department:\n\n" \
               "- Admissions: admit@usiu.ac.ke | +254 730 116 290\n" \
               "- Finance: finance@usiu.ac.ke | +254 730 116 509\n" \
               "- Registrar: Ext 782-790\n" \
               "- Student Affairs: Ext 436\n\n" \
               "Visit www.usiu.ac.ke for more information."


class SupervisorAgent:
    """Orchestrates the multi-agent workflow"""
    
    def __init__(self, knowledge_dir: str = "knowledge"):
        self.router = QueryRouterAgent()
        self.retriever = KnowledgeRetrieverAgent(knowledge_dir)
        self.generator = ResponseGeneratorAgent()
        self.conversation_history = []
    
    def process_query(self, query: str) -> Dict[str, Any]:
        """Main orchestration logic"""
        
        # Step 1: Route query
        category = self.router.route(query)
        
        # Step 2: Retrieve knowledge
        knowledge = self.retriever.retrieve(category, query)
        
        # Step 3: Generate response
        response = self.generator.generate(query, knowledge, category)
        
        # Step 4: Store in history
        self.conversation_history.append({
            "query": query,
            "category": category,
            "response": response
        })
        
        return {
            "query": query,
            "category": category,
            "response": response,
            "sources": list(knowledge.keys()) if knowledge else []
        }
