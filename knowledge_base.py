"""
Tamil Nadu Government Digital Services Knowledge Base (TNeGA, TNPDS, Revenue, EB, Schemes)
Authoritative reference for Makkal AI citizen guidance.
"""

from typing import Dict, Any, List

SERVICES_CATALOG: Dict[str, Dict[str, Any]] = {
    "patta_chitta": {
        "id": "patta_chitta",
        "title_ta": "பட்டா & சிட்டா நில ஆவணங்கள்",
        "title_en": "Patta & Chitta Land Records (Any-ROR)",
        "portal_url": "https://eservices.tn.gov.in/eservicesnew/land/chitta.html",
        "portal_name": "Any-ROR Tamil Nadu Land Records Portal",
        "fee": "இலவசம் (Free online download)",
        "duration": "உடனடி (Instant Download)",
        "required_docs": [
            "மாவட்டம் (District)",
            "வட்டம் (Taluk)",
            "கிராமம் (Village)",
            "சர்வே எண் மற்றும் உட்பிரிவு எண் (Survey No & Sub-division No) அல்லது பட்டா எண் (Patta No)"
        ],
        "procedure_ta": "1. அதிகாரப்பூர்வ Any-ROR போர்ட்டலுக்கு செல்லவும்.\n2. மாவட்டம், வட்டம், கிராமம் தேர்ந்தெடுக்கவும்.\n3. உங்கள் நிலத்தின் பட்டா எண் அல்லது சர்வே எண்ணை உள்ளிடவும்.\n4. திரையில் தோன்றும் கேப்ட்சா குறியீட்டை உள்ளிட்டால் உங்கள் பட்டா/சிட்டா நகல் உடனடியாக PDF வடிவில் பதிவிறக்கம் ஆகும்."
    },
    "ration_card_add_member": {
        "id": "ration_card_add_member",
        "title_ta": "குடும்ப அட்டையில் புதிய உறுப்பினர்/குழந்தை பெயர் சேர்த்தல்",
        "title_en": "TNPDS Smart Ration Card - Add Family Member / New Born Child",
        "portal_url": "https://tnpds.gov.in",
        "portal_name": "TNPDS Official Portal",
        "fee": "இலவசம் (Free)",
        "duration": "15 முதல் 30 வேலை நாட்கள் (15-30 working days)",
        "required_docs": [
            "குழந்தையின் பிறப்புச் சான்றிதழ் (Birth Certificate)",
            "பெற்றோரின் ஆதார் அட்டை நகல் (Parents Aadhaar)",
            "தற்போதைய ஸ்மார்ட் குடும்ப அட்டை (Smart Ration Card)",
            "திருமணமானவராக இருந்தால் முந்தைய ரேஷன் கார்டில் பெயர் நீக்கிய சான்றிதழ் (Surrender/Deletion Certificate)"
        ],
        "procedure_ta": "1. TNPDS அதிகாரப்பூர்வ இணையதளத்தில் உங்கள் பதிவு செய்யப்பட்ட மொபைல் எண் மூலம் OTP பெற்று லாகின் செய்யவும்.\n2. 'மின்னணு அட்டை தொடர்பான சேவைகள்' பகுதியில் 'உறுப்பினர் சேர்க்க' என்பதை கிளிக் செய்யவும்.\n3. புதிய நபரின் விவரங்களை உள்ளிட்டு பிறப்புச் சான்றிதழ் அல்லது ஆதார் நகலை பதிவேற்றவும்.\n4. விண்ணப்ப எண் (Reference Number) SMS-ஆக வரும். வட்ட வழங்கல் அலுவலர் (TSO) சரிபார்த்து அனுமதிப்பார்."
    },
    "community_certificate": {
        "id": "community_certificate",
        "title_ta": "சாதிச் சான்றிதழ் (Community Certificate)",
        "title_en": "e-Sevai Community Certificate",
        "portal_url": "https://tnesevai.tn.gov.in",
        "portal_name": "TNeGA e-Sevai Portal",
        "fee": "₹60 (அரசு கட்டணம்)",
        "duration": "15 வேலை நாட்கள் (15 working days)",
        "required_docs": [
            "விண்ணப்பதாரரின் ஆதார் அட்டை (Aadhaar Card)",
            "தந்தை அல்லது தாய் அல்லது உடன்பிறந்தோரின் சாதிச் சான்றிதழ் (Parent/Sibling Community Cert)",
            "பள்ளி மாற்றுச் சான்றிதழ் (School TC) அல்லது மார்க்ஷீட்",
            "பாஸ்போர்ட் அளவு புகைப்படம்",
            "சுய அறிவிப்புப் படிவம் (Self Declaration Form)"
        ],
        "procedure_ta": "1. e-Sevai போர்ட்டலில் CAN எண்ணை உள்ளிட்டு லாகின் செய்யவும்.\n2. வருவாய்த்துறை சேவைகளில் 'Community Certificate' தேர்ந்தெடுக்கவும்.\n3. தேவையான விவரங்களை உள்ளிட்டு சாதி சான்றிதழ் நகலை பதிவேற்றவும்.\n4. VAO, RI மற்றும் Zonal Deputy Tahsildar ஒப்புதலுக்குப் பின் டிஜிட்டல் கையொப்பமிட்ட சான்றிதழ் பதிவிறக்கம் செய்யலாம்."
    },
    "income_certificate": {
        "id": "income_certificate",
        "title_ta": "வருமானச் சான்றிதழ் (Income Certificate)",
        "title_en": "e-Sevai Annual Income Certificate",
        "portal_url": "https://tnesevai.tn.gov.in",
        "portal_name": "TNeGA e-Sevai Portal",
        "fee": "₹60 (அரசு கட்டணம்)",
        "duration": "7 முதல் 15 வேலை நாட்கள் (7-15 working days)",
        "required_docs": [
            "ஆதார் அட்டை (Aadhaar Card)",
            "குடும்ப அட்டை (Ration Card)",
            "சம்பளச் சீட்டு (Salary Slip) அல்லது வருமான விவர ஆவணம்",
            "பாஸ்போர்ட் அளவு புகைப்படம்",
            "சுய அறிவிப்புப் படிவம்"
        ],
        "procedure_ta": "1. e-Sevai மையத்திலோ அல்லது குடிமக்கள் போர்ட்டலிலோ விண்ணப்பிக்கலாம்.\n2. குடும்பத்தின் அனைத்து வருமான ஆதாரங்களையும் துல்லியமாக குறிப்பிடவும்.\n3. VAO நில விசாரணை செய்து ஒப்புதல் அளித்தவுடன் சான்றிதழ் கிடைக்கும்."
    },
    "tangedco_eb_bill": {
        "id": "tangedco_eb_bill",
        "title_ta": "மின்சார கட்டணம் மற்றும் நுகர்வோர் எண் சேவை",
        "title_en": "TANGEDCO Electricity Bill Payment & Consumer Linking",
        "portal_url": "https://www.tnebnet.org/qwp/qpay",
        "portal_name": "TANGEDCO Quick Pay",
        "fee": "பயன்பாட்டுக்கு ஏற்ப (Based on units consumed, first 100 units free)",
        "duration": "உடனடி ரசீது (Instant Receipt)",
        "required_docs": [
            "மின் நுகர்வோர் எண் (Consumer Number - 10 to 11 digits)",
            "ஆதார் எண்ணுடன் இணைக்கப்பட்ட மொபைல் எண் (Aadhaar Linked Mobile)"
        ],
        "procedure_ta": "1. TANGEDCO Quick Pay இணையதளத்திற்கு செல்லவும்.\n2. உங்கள் பகுதி குறியீடு மற்றும் நுகர்வோர் எண்ணை உள்ளிடவும்.\n3. நடப்பு மாத கட்டணத்தை UPI, NetBanking அல்லது Card மூலம் செலுத்தி உடனடி ரசீதை பெறலாம்."
    },
    "cmchis_health_insurance": {
        "id": "cmchis_health_insurance",
        "title_ta": "முதலமைச்சரின் விரிவான மருத்துவக் காப்பீட்டுத் திட்டம் (CMCHIS)",
        "title_en": "Chief Minister's Comprehensive Health Insurance Scheme (5 Lakhs)",
        "portal_url": "https://www.cmchistn.com",
        "portal_name": "CMCHIS Official Portal",
        "fee": "முற்றிலும் இலவசம் (100% Free Government Scheme)",
        "duration": "மாவட்ட ஆட்சியர் அலுவலகத்தில் உடனடி அட்டை (Immediate smart card at Collectorate)",
        "required_docs": [
            "ஸ்மார்ட் குடும்ப அட்டை (Ration Card)",
            "குடும்ப உறுப்பினர்களின் ஆதார் அட்டைகள்",
            "ஆண்டு வருமானம் ₹1,20,000-க்குள் இருப்பதற்கான வருமானச் சான்றிதழ்",
            "கிராம நிர்வாக அலுவலர் (VAO) சான்றிதழ்"
        ],
        "procedure_ta": "1. தேவையான ஆவணங்களுடன் உங்கள் மாவட்ட ஆட்சியர் அலுவலகத்தில் உள்ள CMCHIS மையத்தை அணுகவும்.\n2. பயோமெட்ரிக் கைரேகை மற்றும் புகைப்படம் எடுக்கப்பட்டு உடனடியாக காப்பீட்டு அட்டை வழங்கப்படும்.\n3. இதன் மூலம் அரசு மற்றும் அங்கீகரிக்கப்பட்ட தனியார் மருத்துவமனைகளில் ஆண்டுக்கு ₹5 லட்சம் வரை கட்டணமில்லா சிகிச்சை பெறலாம்."
    },
    "kalaignar_magalir_urimai": {
        "id": "kalaignar_magalir_urimai",
        "title_ta": "கலைஞர் மகளிர் உரிமைத் திட்டம் (மாதம் ₹1,000)",
        "title_en": "Kalaignar Magalir Urimai Thogai Scheme (₹1,000 / month)",
        "portal_url": "https://kmut.tn.gov.in",
        "portal_name": "KMUT Scheme Portal",
        "fee": "இலவசம்",
        "duration": "நேரடி வங்கி பரிமாற்றம் (Direct Benefit Transfer)",
        "required_docs": [
            "ஸ்மார்ட் குடும்ப அட்டை (குடும்பத் தலைவி பெயர் இருக்க வேண்டும்)",
            "ஆதார் அட்டை (Aadhaar linked with Bank Account)",
            "வங்கி சேமிப்புக் கணக்கு புத்தகம் (Bank Passbook)",
            "மின்சார நுகர்வோர் எண் (Electricity Consumer Number)"
        ],
        "procedure_ta": "1. குடும்ப அட்டை உள்ள குடும்பத் தலைவிக்கு மட்டுமே இந்த உரிமைத் தொகை வழங்கப்படும்.\n2. தகுதிகள்: குடும்ப ஆண்டு வருமானம் ₹2.5 லட்சத்திற்குள் இருக்க வேண்டும்; ஆண்டுக்கு 3600 யூனிட்டுக்கு குறைவான வீட்டு மின் நுகர்வு.\n3. தொகை மாதந்தோறும் 15-ஆம் தேதி வங்கிக் கணக்கில் நேரடியாக வரவு வைக்கப்படும்."
    }
}


def get_service_info(query: str) -> str:
    """Matches citizen query to available Tamil Nadu services and returns structured context."""
    q_lower = query.lower()
    matched = []
    
    keywords = {
        "patta_chitta": ["பட்டா", "சிட்டா", "நிலம்", "சர்வே", "patta", "chitta", "land", "survey"],
        "ration_card_add_member": ["ரேஷன்", "குடும்ப அட்டை", "குழந்தை பெயர்", "உறுப்பினர்", "ration", "tnpds", "baby"],
        "community_certificate": ["சாதி", "சான்றிதழ்", "community", "caste", "tc"],
        "income_certificate": ["வருமானம்", "வருமானச்", "income", "salary"],
        "tangedco_eb_bill": ["மின்சாரம்", "கரண்ட்", "eb", "bill", "tangedco", "electricity"],
        "cmchis_health_insurance": ["காப்பீடு", "மருத்துவம்", "ஆஸ்பத்திரி", "cmchis", "insurance", "hospital", "5 லட்சம்"],
        "kalaignar_magalir_urimai": ["மகளிர்", "உரிமை", "1000", "கலைஞர்", "magalir", "urimai", "kmut"]
    }
    
    for s_id, kw_list in keywords.items():
        if any(kw in q_lower for kw in kw_list):
            matched.append(SERVICES_CATALOG[s_id])
            
    if not matched:
        # Default to top 3 essential services
        matched = [SERVICES_CATALOG["patta_chitta"], SERVICES_CATALOG["ration_card_add_member"], SERVICES_CATALOG["income_certificate"]]
        
    return matched
