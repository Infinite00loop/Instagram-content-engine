from dotenv import load_dotenv
load_dotenv()

from crewai import Crew

from tasks import CampaignTaskDefinitions
from agents import CampaignAgentsFactory

task_factory = CampaignTaskDefinitions()
agent_factory = CampaignAgentsFactory()

print("=========================================")
print("🤖 Welcome to the Instagram Content Engine")
print("=========================================")
target_website = input("Enter the target product website for the campaign:\n")
extra_campaign_details = input("Enter any specific campaign requirements or details:\n")

# Initialize Agents
intel_director = agent_factory.market_intelligence_expert()
strategy_head = agent_factory.head_of_digital_strategy()
copy_lead = agent_factory.lead_brand_copywriter()

# Initialize Tasks for Content Generation
product_intel_task = task_factory.analyze_target_product(intel_director, target_website, extra_campaign_details)
competitor_intel_task = task_factory.evaluate_competitors(intel_director, target_website, extra_campaign_details)
strategy_task = task_factory.develop_campaign_strategy(strategy_head, target_website, extra_campaign_details)
copywriting_task = task_factory.draft_social_media_copy(copy_lead)

# Create Content Engine Crew
content_engine_crew = Crew(
	agents=[
		intel_director,
		strategy_head,
		copy_lead
	],
	tasks=[
		product_intel_task,
		competitor_intel_task,
		strategy_task,
		copywriting_task
	],
	verbose=True
)

final_ad_copy = content_engine_crew.kickoff()

# Initialize Visual Assets Agents
art_director = agent_factory.visual_art_director()
exec_creative_director = agent_factory.executive_creative_director()

# Initialize Visual Tasks
# Assuming final_ad_copy has a .raw attribute or can be cast to string
copy_output = final_ad_copy.raw if hasattr(final_ad_copy, 'raw') else str(final_ad_copy)

concept_task = task_factory.generate_image_prompts(art_director, copy_output, target_website, extra_campaign_details)
approval_task = task_factory.review_creative_assets(exec_creative_director, target_website, extra_campaign_details)

visuals_engine_crew = Crew(
	agents=[
		art_director,
		exec_creative_director
	],
	tasks=[
		concept_task,
		approval_task
	],
	verbose=True
)

final_image_prompts = visuals_engine_crew.kickoff()

# Display Outcomes
print("\n\n" + "="*40)
print("🎯 CAMPAIGN GENERATION COMPLETE")
print("="*40 + "\n")
print("--- APPROVED INSTAGRAM COPY ---")
print(final_ad_copy)
print("\n\n--- APPROVED IMAGE GENERATION PROMPTS ---")
print(final_image_prompts)
print("\n" + "="*40)
