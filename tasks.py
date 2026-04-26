from crewai import Task
from textwrap import dedent

class CampaignTaskDefinitions:
	def analyze_target_product(self, agent, target_url, extra_context):
		return Task(description=dedent(f"""\
			Examine the primary product website: {target_url}.
			Additional client context: {extra_context}.

			Your objective is to extract the core value propositions, unique 
			features, and the overarching brand story being communicated.

			Your final output must be a comprehensive breakdown of the product's 
			primary selling points, its target demographic appeal, and strategic 
			recommendations for market positioning. Highlight exactly what makes 
			this product disruptive or special.

			Remember, granular attention to detail is required. The current year is 2024.
			"""),
			expected_output="An extensive intelligence report detailing product selling points, target demographics, and strategic positioning recommendations.",
			agent=agent
		)

	def evaluate_competitors(self, agent, target_url, extra_context):
		return Task(description=dedent(f"""\
			Investigate the competitive landscape for: {target_url}.
			Additional client context: {extra_context}.

			Locate the top three direct market competitors. Analyze their digital 
			strategies, how they position themselves, and general consumer sentiment.

			Your final output MUST contain a full contextual summary of {target_url} 
			alongside a rigorous, point-by-point comparison against its top three rivals.
			"""),
			expected_output="A thorough competitive analysis report comparing the client's product against its top three market rivals.",
			agent=agent
		)

	def develop_campaign_strategy(self, agent, target_url, extra_context):
		return Task(description=dedent(f"""\
			You are architecting a highly targeted promotional campaign for: {target_url}.
			Additional client context: {extra_context}.

			To launch this initiative, we require a robust strategic framework and 
			innovative content angles. These must be engineered to aggressively 
			capture the attention of the specific target audience.

			Your generated concepts will serve as the blueprint for the creative team.

			Your final output MUST consist of brilliant, audience-specific campaign 
			ideas, incorporating all known context about the product and the client's goals.
			"""),
			expected_output="A strategic blueprint containing highly targeted, innovative campaign ideas and angles.",
			agent=agent
		)

	def draft_social_media_copy(self, agent):
		return Task(description=dedent("""\
			Draft highly engaging Instagram ad copy.
			The text should be sharp, magnetic, succinct, and perfectly in sync 
			with the overarching campaign strategy.

			Concentrate on messaging that deeply resonates with the core demographic 
			while spotlighting the product's unique value.

			The copy must be scroll-stopping and include a strong call-to-action (CTA), 
			whether that is driving traffic to the site, prompting a sale, or encouraging engagement.

			Your final output MUST include 3 distinct variations of Instagram ad copy 
			that educate, thrill, and convert readers.
			"""),
			expected_output="3 distinct, high-converting Instagram ad copy variations with strong CTAs.",
			agent=agent
		)

	def generate_image_prompts(self, agent, approved_copy, target_url, extra_context):
		return Task(description=dedent(f"""\
			You are conceptualizing the visual assets for a flagship client campaign. 
			You MUST draft the ultimate, most visually striking photographic concepts 
			to accompany this specific Instagram copy:
			{approved_copy}

			Product context: {target_url}.
			Additional client context: {extra_context}.

			Visualize the ideal photograph and describe it vividly in a single paragraph.
			Here are structural examples for your prompts:
			- a sleek, futuristic hypercar drifting on a neon-lit cyber-street during a heavy downpour, cinematic lighting, 8k resolution, ultra-detailed wide shot
			- an intense close-up of a barista expertly pouring latte art, moody ambient cafe lighting, depth of field, 4k, crisp focus
			- a serene hiker standing atop a misty mountain peak at dawn, wearing bright orange gear against a cold blue landscape, soft morning light, 4k, drone perspective

			Be deeply creative and focus on visual hooks that stop the scroll. 
			Crucially: DO NOT directly feature the physical product in the concept.

			Your final output must be exactly 3 distinct photographic concepts, 
			each described in 1 paragraph mirroring the format of the examples above.
			"""),
			expected_output="3 distinct visual concepts, each described in a single paragraph suitable for AI image generation.",
			agent=agent
		)

	def review_creative_assets(self, agent, target_url, extra_context):
		return Task(description=dedent(f"""\
			Audit the visual concepts submitted by the Art Director.
			Ensure they are absolute top-tier quality and perfectly align with the 
			strategic brand objectives. Review, greenlight, or mandate revisions 
			to finalize the creative direction.

			Product context: {target_url}.
			Additional client context: {extra_context}.

			As a reminder, acceptable final prompts look like this:
			- a sleek, futuristic hypercar drifting on a neon-lit cyber-street during a heavy downpour, cinematic lighting, 8k resolution, ultra-detailed wide shot
			- an intense close-up of a barista expertly pouring latte art, moody ambient cafe lighting, depth of field, 4k, crisp focus
			- a serene hiker standing atop a misty mountain peak at dawn, wearing bright orange gear against a cold blue landscape, soft morning light, 4k, drone perspective

			Your final output must be the 3 finalized, approved photographic concepts, 
			each detailed in a single descriptive paragraph.
			"""),
			expected_output="3 finalized and approved visual concepts, formatted as single-paragraph image generation prompts.",
			agent=agent
		)