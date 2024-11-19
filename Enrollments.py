import re
from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt
import openai
import textwrap

# Define regions and corresponding countries
regions = {
    'Central & Eastern Europe': [
        "Albania", "BosniaandHerzegovina", "Bulgaria", "Croatia", "Cyprus",
        "CzechRepublic", "Estonia", "FormerYugoslavRepublicofMacedonia",
        "Greece", "Hungary", "Kosovo", "Latvia", "Lithuania", "Montenegro",
        "Poland", "Romania", "Serbia", "Slovakia", "Slovenia"],

    'Central Asia (CIS)': [
        "Armenia", "Azerbaijan", "Belarus", "Georgia",
        "Kazakhstan", "Kyrgyzstan", "Moldova",
        "Tajikistan", "Ukraine", "Uzbekistan"],

    'East, Southeast Asia & Pacific': [
        "AmericanSamoa", "Australia", "Brunei", "Cambodia", "China",
        "Christmas Island", "Cocos (Keeling) Islands", "Cook Islands",
        "EastTimor", "Federated States of Micronesia", "Fiji",
        "French Polynesia", "Guam", "Heard Island and McDonald Islands",
        "HongKong", "Japan", "Kiribati", "Laos", "Macau", "Malaysia",
        "Marshall Islands", "Mongolia", "Myanmar", "Nauru", "New Caledonia",
        "New Zealand", "Niue", "Norfolk Island", "North Korea",
        "Northern Mariana Islands", "Palau", "Papua New Guinea", "Philippines",
        "Pitcairn Islands", "Samoa", "Singapore", "Solomon Islands",
        "SouthKorea", "Taiwan", "Thailand", "Tokelau", "Tonga", "Tuvalu",
        "United States Minor Outlying Islands", "Vanuatu", "Vietnam", "Samoa", "Japan", "Macau ", "Vanuatu"],

    'Indonesia': ["Indonesia"],

    'Iran': ["Iran"],

    'Latin America & The Caribbean': [
        "Anguilla", "AntiguaandBarbuda", "Argentina", "Aruba", "Barbados",
        "Belize", "Bermuda", "Bolivia", "Bouvet Island", "Brazil",
        "British Virgin Islands", "Caribbean Netherlands", "Cayman Islands",
        "Chile", "Colombia", "Costa Rica", "Cuba", "Curaçao", "Dominica",
        "Dominican Republic", "Ecuador", "El Salvador", "Falkland Islands",
        "French Guiana", "Grenada", "Guadeloupe", "Guatemala", "Guyana",
        "Haiti", "Honduras", "Jamaica", "Martinique", "Mexico", "Montserrat",
        "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico",
        "Saint Barthélemy", "SaintKittsandNevis", "SaintLucia",
        "Saint Vincent and the Grenadines", "Saint-Martin", "Sint Maarten",
        "Suriname", "The Bahamas", "Trinidad and Tobago", "Turks and Caicos Islands",
        "United States Virgin Islands", "Uruguay", "Venezuela"
    ],

    'MENA': [
        "Akrotiri and Dhekelia", "Algeria", "Bahrain", "British Indian Ocean Territory",
        "Egypt", "Iraq", "Israel", "Jordan", "Kuwait", "Lebanon", "Libya",
        "Morocco", "Oman", "Palestine", "Qatar", "Sahrawi Arab Democratic Republic",
        "SaudiArabia", "Syria", "Tunisia", "UnitedArabEmirates", "Yemen"
    ],

    'North America': ["Canada", "UnitedStates"],

    'Northern & Western Europe': [
        "Aland", "Andorra", "Austria", "Belgium", "Denmark", "Faroe Islands",
        "Finland", "France", "Germany", "Gibraltar", "Greenland", "Guernsey",
        "Iceland", "Ireland", "Isle of Man", "Italy", "Jersey", "Liechtenstein",
        "Luxembourg", "Malta", "Monaco", "Netherlands", "Norway", "Portugal",
        "San Marino", "Spain", "Svalbard and Jan Mayen", "Sweden", "Switzerland",
        "UnitedKingdom", "Vatican City"
    ],

    'Russia': ["Russia"],

    'South Asia': [
        "Afghanistan", "Bangladesh", "Bhutan", "India", "Maldives",
        "Nepal", "Pakistan", "SriLanka"
    ],

    'Sub-Saharan Africa': [
        "Angola", "Benin", "Botswana", "BurkinaFaso", "Burundi", "Cameroon",
        "Cape Verde", "CentralAfricanRepublic", "Chad", "Comoros", "DemocraticRepublicoftheCongo", "Congo",
        "Djibouti", "EquatorialGuinea", "Eritrea", "Eswatini", "Ethiopia",
        "French Southern and Antarctic Lands", "Gabon", "Ghana", "Guinea",
        "Guinea-Bissau", "IvoryCoast", "Kenya", "Lesotho", "Liberia",
        "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Mayotte",
        "Mozambique", "Namibia", "Niger", "Nigeria", "Réunion", "Rwanda",
        "Saint Helena, Ascension and Tristan da Cunha", "São Tomé and Príncipe",
        "Senegal", "Seychelles", "SierraLeone", "Somalia", "SouthAfrica",
        "SouthSudan", "Sudan", "Swaziland", "Tanzania", "TheGambia", "Togo",
        "Uganda", "Zambia", "Zimbabwe"
    ],

    'Türkiye': ["TurkishRepublicofNorthernCyprus", "Turkey"],
    'Turkmenistan': ["Turkmenistan"],
}

# Configure OpenAI API Key
openai.api_key = "sk-proj-_PEN5ED8JJG5BOXNrGJy=9vyyMKUcP-2rwOssiLQrYGa-8OFgMA"



# Function to clean column names
def camel_to_snake(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower().replace(" ", "_")


# Function to clean text for PDF
def clean_text(text):
    if text is None:
        return "No recommendations available for this region."
    return text.encode("latin-1", "replace").decode("latin-1")

# Function to get region by country
def get_region_by_country(country):
    for region, countries in regions.items():
        if country in countries:
            return region
    return "Unknown"

# Function to generate AI recommendations
def generate_ai_recommendations(region, paid_data, applied_data, data):
    try:
        # Validate inputs
        if paid_data.empty or applied_data.empty:
            return f"No sufficient data for {region} to generate recommendations."

        # Summarize data for the region
        summary = f"Region: {region}\n\n"
        summary += "Top Programs by Revenue (Paid):\n"
        for program, revenue in paid_data.items():
            summary += f"- {program}: ${revenue:,.2f}\n"
        summary += "\nTop Programs by Applications (Applied):\n"
        for program, count in applied_data.items():
            summary += f"- {program}: {count} applications\n"

        # Data Preparation for Each Region
        regions = data["region"].unique()

        # Dictionary to hold region-specific data
        region_specific_data = {}

        for region in regions:
            # Filter data for the current region
            region_data = data[data["region"] == region]

            if region_data.empty:
                print(f"No data available for region: {region}")
                region_specific_data[region] = {
                    "applications_and_payments": {"total_applications": 0, "total_revenue": 0},
                    "popular_majors": {},
                    "low_performing_majors": {},
                    "digital_marketing_effectiveness": {
                        "Facebook": "Data unavailable",
                        "Google Ads": "Data unavailable",
                        "LinkedIn": "Data unavailable",
                        "Instagram": "Data unavailable"
                    },
                }
                continue  # Skip to the next region

            # Applications and Payments for this region
            try:
                applications_and_payments = region_data.agg(
                    total_applications=("id", "count"),
                    total_revenue=("current_revenue", "sum")
                ).fillna(0).to_dict()
            except Exception as e:
                print(f"Error aggregating applications and payments for {region}: {e}")
                applications_and_payments = {"total_applications": 0, "total_revenue": 0}

            # Popular Majors for this region
            try:
                popular_majors = region_data.groupby("program").agg(
                    total_applications=("id", "count")
                ).sort_values(by="total_applications", ascending=False).head(10).to_dict()
            except Exception as e:
                print(f"Error finding popular majors for {region}: {e}")
                popular_majors = {}

            # Low-Performing Majors for this region
            try:
                low_performing_majors = region_data.groupby("program").agg(
                    total_applications=("id", "count"),
                    total_revenue=("current_revenue", "sum")
                ).sort_values(by=["total_applications", "total_revenue"]).head(10).to_dict()
            except Exception as e:
                print(f"Error finding low-performing majors for {region}: {e}")
                low_performing_majors = {}

            # Digital Marketing Effectiveness (placeholder or actual data)
            digital_marketing_effectiveness = {
                "Facebook": "High engagement",
                "Google Ads": "Moderate conversions",
                "LinkedIn": "Low engagement",
                "Instagram": "Not available in some regions (e.g., Russia)"
            }

            # Store data for the region
            region_specific_data[region] = {
                "applications_and_payments": applications_and_payments,
                "popular_majors": popular_majors,
                "low_performing_majors": low_performing_majors,
                "digital_marketing_effectiveness": digital_marketing_effectiveness,
            }

        # Print a summary of the prepared data
        for region, data in region_specific_data.items():
            print(f"Prepared data for {region}: {data}")

        # Prompt Creation for Each Region
        for region, data in region_specific_data.items():
            prompt = f"""
                    You are an AI strategist specializing in education, marketing, and operational planning. Based on the following data for the region "{region}", analyze trends and develop a comprehensive plan to market both low-performing and high-performing majors. Your strategy should address both regional and global contexts to maximize applications and revenue.

                    Your analysis and plan should include the following:

                    1. **Regional Insights**:
                        - Analyze application and payment volumes for this region.
                        - Highlight student preferences for both high-performing and low-performing majors.
                        - Provide a demographic and cultural overview to identify key marketing opportunities and challenges.

                    2. **Marketing Strategies for High-Performing Majors**:
                        - Propose strategies to sustain and grow applications for high-performing majors.
                        - Suggest digital marketing platforms suitable for this region (e.g., Facebook, VKontakte, WeChat).
                        - Recommend leveraging testimonials, alumni success stories, and industry partnerships.

                    3. **Marketing Strategies for Low-Performing Majors**:
                        - Provide actionable strategies to improve visibility and interest in low-performing majors.
                        - Propose creative campaigns to address common barriers like affordability or perceived value.
                        - Recommend using targeted ads, influencer partnerships, webinars, or demo courses.

                    4. **Digital Transformation for the Region**:
                        - Highlight technologies like AI chatbots, CRM systems, and predictive analytics for engagement.
                        - Suggest improvements for the website and mobile platforms to cater to this region.
                        - Propose multilingual and localized content strategies for inclusivity.

                    5. **Financial Optimization**:
                        - Recommend tuition fee strategies with localized adjustments based on affordability and demand.
                        - Suggest scholarship campaigns targeting underrepresented demographics.
                        - Propose methods to improve ROI on marketing investments for this region.

                    6. **Future Challenges and Opportunities**:
                        - Identify regional challenges like regulatory changes, economic trends, or competition.
                        - Highlight growth opportunities such as partnerships, online programs, or interdisciplinary studies.
                        - Recommend strategies to stay competitive in the region.

                    7. **Innovation and Creativity**:
                        - Propose unique initiatives like dual-degree programs, gamified learning, or experiential workshops.
                        - Recommend trends like sustainability or experiential learning to differentiate the institution.

                    8. **Summary and Roadmap**:
                        - Summarize key takeaways, including strengths, weaknesses, opportunities, and threats (SWOT analysis).
                        - Provide a prioritized roadmap with timelines and key performance indicators (KPIs) for success.
                        - Suggest methods for ongoing tracking and evaluation to adapt strategies dynamically.

                    Here is the specific data for "{region}":

                    - Applications and payments: {data['applications_and_payments']}
                    - Popular majors: {data['popular_majors']}
                    - Low-performing majors: {data['low_performing_majors']}
                    - Digital marketing effectiveness: {data['digital_marketing_effectiveness']}

                    If any information is missing, provide recommendations based on your expertise, trends, and assumptions to ensure a complete and actionable strategy.
                """
            # GPT Call
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an AI strategist specializing in education and marketing."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=2000,
                temperature=0.7
            )
            # Return the AI-generated content
            return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error generating recommendations for region {region}: {e}")
        return "Unable to generate recommendations due to an error."


# Load data
data = pd.read_excel("assets/modified_file_specific.xlsx")  # Ensure this path is correct
data.columns = data.columns.map(camel_to_snake)  # Convert column names to snake_case

# Add region information based on country
data['region'] = data['country'].apply(get_region_by_country)

# Filter for 'paid' and 'applied' statuses
paid_data = data[data['status'].str.lower() == "paid"]
applied_data = data[data['status'].str.lower() == "applied"]

# Analyze top 15 programs per region for 'paid' and 'applied'
top_programs_per_region = {}
regions = data["region"].unique()

for region in regions:
    region_paid = paid_data[paid_data["region"] == region]
    region_applied = applied_data[applied_data["region"] == region]

    top_paid = region_paid.groupby("program")["current_revenue"].sum().sort_values(ascending=False).head(15)
    top_applied = region_applied.groupby("program")["id"].count().sort_values(ascending=False).head(15)

    top_programs_per_region[region] = {"paid": top_paid, "applied": top_applied}



# Generate graphs and recommendations
region_strategies = {}
region_graphs = {}

for region, programs in top_programs_per_region.items():
    # Generate AI recommendations
    recommendations = generate_ai_recommendations(region, programs["paid"], programs["applied"], data)
    if not recommendations:
        recommendations = f"Unable to generate recommendations for {region} due to insufficient data or an error."
    region_strategies[region] = recommendations

    # Paid Graph
    plt.figure(figsize=(10, 6))
    programs["paid"].plot(kind="bar", color="skyblue")
    plt.title(f"Top 15 Programs by Revenue (Paid) - {region}")
    plt.ylabel("Revenue")
    plt.xlabel("Program")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    paid_graph_path = f"{region}_paid_top_programs.png"
    plt.savefig(paid_graph_path)
    plt.close()

    # Applied Graph
    plt.figure(figsize=(10, 6))
    programs["applied"].plot(kind="bar", color="orange")
    plt.title(f"Top 15 Programs by Applications (Applied) - {region}")
    plt.ylabel("Applications")
    plt.xlabel("Program")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    applied_graph_path = f"{region}_applied_top_programs.png"
    plt.savefig(applied_graph_path)
    plt.close()

    region_graphs[region] = {"paid": paid_graph_path, "applied": applied_graph_path}


# Create PDF
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "AI-Driven Strategy Report", align="C", ln=True)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")


pdf = PDF()
pdf.add_page()

# Add content for each region
for region, graphs in region_graphs.items():
    # Region title
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, f"Region: {region}", ln=True)
    pdf.set_font("Arial", "", 12)

    # Paid section
    pdf.cell(0, 10, "Top 15 Programs by Revenue (Paid):", ln=True)
    pdf.image(graphs["paid"], x=10, y=None, w=190)
    pdf.ln(10)

    # Applied section
    pdf.cell(0, 10, "Top 15 Programs by Applications (Applied):", ln=True)
    pdf.image(graphs["applied"], x=10, y=None, w=190)
    pdf.ln(10)

    # Recommendations
    pdf.cell(0, 10, "AI-Generated Recommendations:", ln=True)
    recommendations = clean_text(region_strategies.get(region))
    pdf.multi_cell(0, 10, recommendations)
    pdf.ln(20)

# Save PDF
pdf.output("AI_Driven_Strategy_Report.pdf")
print("\nPDF report generated as 'AI_Driven_Strategy_Report.pdf'.")