from pydantic import BaseModel

class LinkFlairRichtext(BaseModel):
	e: str
	t: str


class AuthorFlairRichtext(BaseModel):
	e: str
	t: str


class Source(BaseModel):
	height: int
	url: str
	width: int


class Resolutions(BaseModel):
	height: int
	url: str
	width: int


class Images(BaseModel):
	Resolutions: list[Resolutions]
	id: str
	source: Source
	variants: dict


class Preview(BaseModel):
	Images: list[Images]
	enabled: bool


class ResizedIcons(BaseModel):
	height: int
	url: str
	width: int


class ResizedStaticIcons(BaseModel):
	height: int
	url: str
	width: int


class AllAwardings(BaseModel):
	ResizedIcons: list[ResizedIcons]
	ResizedStaticIcons: list[ResizedStaticIcons]
	award_sub_type: str
	award_type: str
	awardings_required_to_grant_benefits: None
	coin_price: int
	coin_reward: int
	count: int
	days_of_drip_extension: None
	days_of_premium: None
	description: str
	end_date: None
	giver_coin_reward: None
	icon_format: str
	icon_height: int
	icon_url: str
	icon_width: int
	id: str
	is_enabled: bool
	is_new: bool
	name: str
	penny_donate: None
	penny_price: int
	start_date: None
	static_icon_height: int
	static_icon_url: str
	static_icon_width: int
	sticky_duration_seconds: None
	subreddit_coin_reward: int
	subreddit_id: None
	tiers_by_required_awardings: None


class Data(BaseModel):
	AllAwardings: list[AllAwardings]
	AuthorFlairRichtext: list[AuthorFlairRichtext]
	Awarders: list
	LinkFlairRichtext: list[LinkFlairRichtext]
	ModReports: list
	TreatmentTags: list
	UserReports: list
	allow_live_comments: bool
	approved_at_utc: None
	approved_by: None
	archived: bool
	author: str
	author_flair_background_color: str
	author_flair_css_class: None
	author_flair_template_id: str
	author_flair_text: str
	author_flair_text_color: str
	author_flair_type: str
	author_fullname: str
	author_is_blocked: bool
	author_patreon_flair: bool
	author_premium: bool
	banned_at_utc: None
	banned_by: None
	can_gild: bool
	can_mod_post: bool
	category: None
	clicked: bool
	content_categories: None
	contest_mode: bool
	created: float
	created_utc: float
	discussion_type: None
	distinguished: str
	domain: str
	downs: int
	edited: bool
	gilded: int
	gildings: dict
	hidden: bool
	hide_score: bool
	id: str
	is_created_from_ads_ui: bool
	is_crosspostable: bool
	is_meta: bool
	is_original_content: bool
	is_reddit_media_domain: bool
	is_robot_indexable: bool
	is_self: bool
	is_video: bool
	likes: None
	link_flair_background_color: str
	link_flair_css_class: str
	link_flair_template_id: str
	link_flair_text: str
	link_flair_text_color: str
	link_flair_type: str
	locked: bool
	media: None
	media_embed: dict
	media_only: bool
	mod_note: None
	mod_reason_by: None
	mod_reason_title: None
	name: str
	no_follow: bool
	num_comments: int
	num_crossposts: int
	num_reports: None
	over_18: bool
	parent_whitelist_status: None
	permalink: str
	pinned: bool
	post_hint: str
	preview: Preview
	pwls: None
	quarantine: bool
	removal_reason: None
	removed_by: None
	removed_by_category: None
	report_reasons: None
	saved: bool
	score: int
	secure_media: None
	secure_media_embed: dict
	selftext: str
	selftext_html: str
	send_replies: bool
	spoiler: bool
	stickied: bool
	subreddit: str
	subreddit_id: str
	subreddit_name_prefixed: str
	subreddit_subscribers: int
	subreddit_type: str
	suggested_sort: str
	thumbnail: str
	thumbnail_height: None
	thumbnail_width: None
	title: str
	top_awarded_type: None
	total_awards_received: int
	ups: int
	upvote_ratio: float
	url: str
	view_count: None
	visited: bool
	whitelist_status: None
	wls: None


class Children(BaseModel):
	data: Data
	kind: str


class Data(BaseModel):
	Children: list[Children]
	after: str
	before: None
	dist: int
	geo_filter: None
	modhash: str


class Root(BaseModel):
	data: Data
	kind: str


