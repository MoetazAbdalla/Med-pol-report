import re
from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt
import openai
import plotly.express as px
import smtplib
from email.mime.text import MIMEText
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# Configure OpenAI API Key
openai.api_key = "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"

# Function to clean column names
def camel_to_snake(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower().replace(" ", "_")

# Function to clean text for PDF
def clean_text(text):
    if text is None:
        return "No recommendations available for this region."
    return text.encode("latin-1", "replace").decode("latin-1")

# Marketing Automation: Send automated email campaigns
def send_email(subject, content, recipients):
    try:
        sender_email = "your-email@example.com"
        sender_password = "your-password"
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            for recipient in recipients:
                msg = MIMEText(content)
                msg['Subject'] = subject
                msg['From'] = sender_email
                msg['To'] = recipient
                server.sendmail(sender_email, recipient, msg.as_string())
        logging.info("Emails sent successfully.")
    except Exception as e:
        logging.error(f"Error sending emails: {e}")

# Predictive Analytics: Conversion Rate Analysis
def predict_conversion(data):
    try:
        features = data[['applications', 'revenue', 'scholarships']]
        target = data['converted']

        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
        model = LogisticRegression()
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        logging.info(f"Conversion Rate Prediction Accuracy: {accuracy:.2f}")
        return classification_report(y_test, predictions)
    except Exception as e:
        logging.error(f"Error in predictive analytics: {e}")
        return "Predictive analytics failed."

# Function to generate AI recommendations
def generate_ai_recommendations(region, paid_data, applied_data):
    try:
        # Summarize data for the region
        summary = f"Region: {region}\n\n"
        summary += "Top Programs by Revenue (Paid):\n"
        for program, revenue in paid_data.items():
            summary += f"- {program}: ${revenue:,.2f}\n"

        summary += "\nTop Programs by Applications (Applied):\n"
        for program, count in applied_data.items():
            summary += f"- {program}: {count} applications\n"

        # GPT prompt
        prompt = f"""
            You are an AI strategist specializing in education, marketing, and operational planning. Based on the following data for the region "{region}", create a detailed future plan for the next year. Your future plan should address:

            1. Marketing and Outreach (Google Ads, Email Campaigns, Social Media Insights)
            2. Program Performance Improvement
            3. Digital Transformation (AI chatbots, CRM integration, Website Optimization)
            4. Predictive Analytics (Dropout Prediction, Conversion Rate Analysis)
            5. Community Engagement and Social Responsibility
            6. Summary and Key Takeaways

            {summary}

            - Total applications: 
            - Revenue by program: 
            - Applications by nationality: 
            - Digital marketing effectiveness: 
        """
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI strategist specializing in education and marketing."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000,
            temperature=0.7
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        logging.error(f"Error generating recommendations for region {region}: {e}")
        return "Unable to generate recommendations due to an error."

# Load data
data = pd.read_excel("assets/modified_file_specific.xlsx")
data.columns = data.columns.map(camel_to_snake)

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
    region_strategies[region] = generate_ai_recommendations(region, programs["paid"], programs["applied"])

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

# Predictive analytics example
predictive_report = predict_conversion(data)

# Send email summary
send_email(
    subject="AI-Driven Strategy Report",
    content="Your AI-driven strategy report is ready. Please review the attached PDF for insights.",
    recipients=["recipient1@example.com", "recipient2@example.com"]
)

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
