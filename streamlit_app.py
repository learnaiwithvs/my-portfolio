import streamlit as st

# Page configuration
st.set_page_config(page_title="Vikramjit Singh | Portfolio", layout="wide")

# --- HEADER SECTION ---
st.title("Vikramjit Singh")
st.subheader("Software Project Manager | Team Lead | Agile & Scrum Specialist")
st.markdown("📍 Hyderabad, India (Open to relocation to Australia)")
st.markdown("📞 (+91) 9781381213 | ✉️ kuwar.vikram@gmail.com")
st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/vsasr)")

st.write("---")

# --- PROFESSIONAL SUMMARY ---
st.header("Professional Summary")
st.write("""
Software Project Manager and Team Lead with 18+ years delivering enterprise software for Australian and Indian markets 
including RTO/VET compliance systems (AVETMISS, CRICOS, VFH/VSL) and EdTech platforms. 
Proven in leading cross-functional Agile/Scrum teams and applying Lean Six Sigma principles. 
Deep familiarity with the Australian VET sector and available immediately.
""")

# --- WHY HIRE ME / AUSTRALIAN ALIGNMENT ---
st.header("Why I'm a Strong Fit for Australian Employers")
col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🇦🇺 Domain & Workplace")
    st.write("- **Domain:** AVETMISS, CRICOS, VFH/VSL compliance frameworks.")
    st.write("- **Alignment:** Direct collaboration with Sydney-based teams (Truly Imagine, SSBT).")
with col2:
    st.markdown("### 📈 Delivery & Quality")
    st.write("- **Metrics:** 95%+ on-time delivery; 30% reduction in sprint carry-over.")
    st.write("- **Mindset:** Certified Lean Six Sigma practitioner focusing on data-driven solutions.")

# --- CORE COMPETENCIES ---
st.header("Core Competencies")
cols = st.columns(2)
with cols[0]:
    st.write("**Methodologies:** Agile, Scrum, Kanban, Lean Six Sigma, Waterfall, SDLC")
    st.write("**Project Tools:** Jira, Confluence, Asana, Trello, Monday.com, Teamwork, Zendesk")
    st.write("**Agile:** Sprint planning, backlog grooming, velocity tracking, OKRs/KPIs")
    st.write("**QA/Dev:** UI/Functional testing, TestRail, Postman, GitHub, GitLab, Release Management")
with cols[1]:
    st.write("**Data:** MS SQL, PostgreSQL, Power BI & Tableau (awareness), Advanced Excel")
    st.write("**AU Domain:** AVETMISS, CRICOS, VFH/VSL, RTO software, USI Integration")
    st.write("**Leadership:** Stakeholder management, risk mitigation, budget management")
    st.write("**Collaboration:** MS Teams, Slack, Miro, SharePoint, Google Workspace")

# --- WORK EXPERIENCE ---
st.header("Work Experience")

st.subheader("Software Project Manager | Truly Imagine Pty Ltd")
st.caption("Remote - Australian-based company | Jan 2023 - May 2025")
st.write("- Led cross-functional team of 6 using Scrum with 95%+ on-time delivery.")
st.write("- Reduced sprint carry-over by 30% via Jira/Confluence retrospectives.")
st.write("- Owned end-to-end product roadmap and aligned milestones to business OKRs.")
st.write("- Reduced post-release defects by 25% through specialized QA strategies.")
st.write("- Streamlined API integration via GitHub/GitLab and Postman.")

st.subheader("Freelance Project Management Consulting")
st.caption("Apr 2022 - Dec 2022")
st.write("- Completed Atlassian Jira and Lean Six Sigma (White to Advanced Yellow) certifications.")
st.write("- Provided advisory for team workflow optimization for small-scale clients.")

st.subheader("Software Project Manager | Sydney School of Business & Technology")
st.caption("India (Client: Australian RTO) | Jul 2021 - Apr 2022")
st.write("- Delivered ISTUDI platform from requirements to go-live in under 10 months.")
st.write("- Managed backlog of 120+ user stories with Australian product owners.")
st.write("- Conducted sprint reviews with Sydney-based stakeholders to validate delivery.")
st.write("- Ensured data integrity aligned with Australian education reporting (MS SQL/PostgreSQL).")

st.subheader("Database Administrator & Product Manager | Total Synergy Concepts")
st.caption("Amritsar (Client: Australian RTO software) | Nov 2019 - Jun 2021")
st.write("- Managed product improvement sprints using Teamwork and Zendesk.")
st.write("- Supported AVETMISS reporting accuracy through MS SQL and Excel analysis.")
st.write("- Maintained risk register ensuring zero compliance-impacting defects at release.")

st.subheader("Senior Product Support Manager / Team Lead | Dream Net Software")
st.caption("Amritsar (Australian-focused RTO software) | Nov 2008 - Oct 2019")
st.write("- Translated requirements into user stories meeting CRICOS and AVETMISS standards.")
st.write("- Reduced average client onboarding time by 35% through SQL templates.")
st.write("- Mentored junior staff, reducing first-response resolution time by 20%.")

st.subheader("WFM Executive / SME / Technical Support | Kochar InfoTech")
st.caption("Oct 2005 - Oct 2008")
st.write("- Managed workforce scheduling for major telecom clients (Airtel, Aircel, Idea).")
st.write("- Implemented performance improvement plans to increase operational efficiency.")

# --- KEY PROJECTS ---
st.header("Key Projects")
st.write("**EduRP SMS (2024-Present):** Redesigned Finance Module and WhatsApp integration.")
st.write("**ISTUDI SMS (2021-2022):** 10-month full-stack delivery compliant with Australian AVETMISS data standards.")

# --- EMERGING TECH & AI ---
st.header("AI Tools & Adoption")
st.write("- **ChatGPT & Claude:** Prompt engineering for user stories and reports.")
st.write("- **Notion/Confluence AI:** AI-assisted knowledge management.")
st.write("- **AI Analytics:** Exploring Power BI Copilot for real-time reporting.")

# --- CERTIFICATIONS & EDUCATION ---
st.header("Certifications & Education")
st.table({
    "Certification": ["Jira Foundation", "Lean Six Sigma Yellow Belt", "LSS White Belt", "PMP", "Scrum Master"],
    "Body": ["Atlassian", "Daniel Holzer", "Opex Learning", "PMI", "Scrum Alliance"],
    "Status/Date": ["Jun 2022", "Jul 2022", "Jun 2022", "In Progress (2025)", "Planned (2025)"]
})

st.write("**Bachelor of Computer Applications (BCA)** - Hindu College (2003-2006)")

# --- REFEREES ---
st.write("---")
st.write("**Referees:** Professional and Australian-based references available on request.")
