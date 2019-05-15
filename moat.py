"""
TODO:
- Function to load metrics config JSON
- Figure out how to handle Tiles and their tile types
- Try/Fail Logic
- Synchronous?
"""

import argparse
import datetime
import json
import logging
import os
import requests
import sys
from time import sleep
import pandas as pd

TOKEN = os.environ['MOAT_TOKEN']

"""
logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(description='Update Moat')

parser.add_argument('-s','--startdate',type=str, help='YYYY-MM-DD')
parser.add_argument('-e','--enddate',type=str, help='YYYY-MM-DD')
parser.add_argument('-p','--prod', help='send to prod database (cloud)',action='store_true')

args = parser.parse_args()

logging.debug(args)

if args.startdate:
    START_DATE = args.startdate
    END_DATE = args.enddate
else:
    START_DATE = END_DATE = (datetime.datetime.today()-datetime.timedelta(days=1)).strftime('%Y-%m-%d')

with open('moat_config.json', encoding='utf-8') as data_file:
        config = json.loads(data_file.read())

with open('config.json', encoding='utf-8') as data_file:
        db_creds = json.loads(data_file.read())


dimensions = config['request_dimensions']
"""

moat_metrics = {'disp_metrics':['loads_unfiltered',
            'loads_git',
            'impressions_analyzed',
            'l_perc',
            'susp_human',
            'susp_human_perc',
            'in_view_measurable_unfiltered_percent',
            'in_view_measurable_git_percent',
            'in_view_measurable_percent',
            'om_sdk_measurable_rate',
            'swf_img_loads',
            'l_mobile',
            'l_mobile_not_iframe',
            'scroll_measurable_impressions',
            'l_somehow_measurable_unfiltered',
            'l_somehow_measurable_git',
            'measurable_impressions',
            'om_sdk_measurable_imps',
            'mm_hostile_iframe_perc',
            'avg_real_estate_perc',
            'fifty_pct_onscreen_imps',
            'fifty_pct_onscreen_perc',
            'avg_fifty_pct_onscreen_time',
            'in_vp_meas',
            'in_vp',
            'in_vp_perc',
            'px_or_strict_js_ots_unfiltered',
            'px_or_strict_js_ots_git',
            'in_view_impressions',
            'in_view_unfiltered_percent',
            'in_view_git_percent',
            'in_view_percent',
            'dentsu_display_ots',
            'dentsu_display_ots_perc',
            'l_full_visibility_measurable',
            'l_full_visibility_ots',
            'l_full_visibility_ots_percent',
            'l_full_visibility_ots_1_sec',
            'l_full_visibility_ots_1_sec_percent',
            'susp_human_and_inview_meas_sum',
            'susp_human_and_inview_meas_perc',
            'human_and_viewable',
            'human_and_viewable_perc',
            'human_and_dentsu_display_ots',
            'human_and_dentsu_display_ots_perc',
            'susp_human_and_inview_gm_meas_sum',
            'susp_human_and_inview_gm_meas_perc',
            'human_and_viewable_gm',
            'human_and_viewable_gm_perc',
            'human_and_fos_or_large_sum',
            'human_and_fos_or_large_perc',
            'groupm_display_imps',
            'groupm_display_perc',
            'full_vis_2_sec_continuous_inview',
            'full_vis_2_sec_continuous_inview_percent',
            'human_and_groupm_payable_sum',
            'global_groupm_payable_sum',
            'active_in_view_time',
            'iva',
            'iva_percent',
            'ivb',
            'ivb_percent',
            'ivc',
            'ivc_percent',
            'ivd',
            'ivd_percent',
            'ive',
            'ive_percent',
            'active_exposure_time',
            'active_exposure_time_hr',
            'average_minute_audience',
            'universal_interactions',
            'universal_interactions_percent',
            'universal_interaction_time_sum',
            'universal_interaction_time',
            'total_ad_dwell_time',
            'hovers',
            'hovers_percent',
            'time_to_hover_sum',
            'time_to_hover',
            'attention_quality',
            'universal_touches',
            'universal_touch_percent',
            'time_to_touch_sum',
            'time_to_touch',
            'scrolls',
            'time_to_scroll_percent',
            'sum_of_times_to_scroll',
            'time_to_scroll',
            'passthrough_imps',
            'passthrough_rate',
            'sum_of_dwell_times',
            'page_dwell_time',
            'c1_unfiltered',
            'c1_git',
            'clicks',
            'clicks_unfiltered_percent',
            'clicks_git_percent',
            'clicks_percent',
            'loaded_btf_fixed_count',
            'loaded_btf_fixed_percent',
            'gold_below_the_fold_count',
            'gold_below_the_fold_percent',
            'never_focused_count',
            'never_focused_percent',
            'never_visible_count',
            'never_visible_percent',
            'never_50_per_visible_count',
            'never_50_perc_visible_percent',
            'never_1_sec_visible_count',
            'never_1_sec_visible_percent',
            'grapeshot_measurable_percent',
            'grapeshot_safe_percent',
            'grapeshot_unsafe_percent',
            'grapeshot_adult_percent',
            'grapeshot_arms_percent',
            'grapeshot_crime_percent',
            'grapeshot_death_injury_percent',
            'grapeshot_illegal_downloads_percent',
            'grapeshot_drugs_percent',
            'grapeshot_hate_speech_percent',
            'grapeshot_military_percent',
            'grapeshot_obscenity_percent',
            'grapeshot_terrorism_percent',
            'grapeshot_tobacco_percent',
            'susp_l_measurable_perc',
            'susp_bot_perc',
            'givt_rate',
            'sivt_rate',
            'susp_bot_browser_perc',
            'susp_bot_susp_browser_perc',
            'susp_bot_data_center_perc',
            'susp_bot_spider_perc',
            'susp_ms_abf_perc',
            'susp_bad_domain_perc',
            'susp_bot_proxy_perc',
            'ad_hidden_perc',
            'susp_bot_geo_perc',
            'susp_old_browser_perc',
            'susp_late_night_perc',
            'susp_top_hour_perc',
            'mm_no_referrer_perc',
            'mm_history_avg',
            'susp_incentivized_perc',
            'session_hijacked_perc',
            'moat_score'],

'vid_metrics':['loads_unfiltered',
            'loads_git',
            'impressions_analyzed',
            'l_perc',
            'susp_human',
            'susp_human_perc',
            'susp_human_and_inview_meas_sum',
            'susp_human_and_inview_meas_perc',
            'human_and_viewable',
            'human_and_viewable_perc',
            'human_and_inview_3sec_cumulative',
            'human_and_inview_3sec_cumulative_perc',
            'human_and_fully_on_screen_3sec_cumulative',
            'human_and_fully_on_screen_3sec_cumulative_perc',
            'video_full_vis_half_the_time',
            'video_full_vis_half_the_time_perc',
            'susp_human_and_inview_gm_meas_sum',
            'susp_human_and_inview_gm_meas_perc',
            'human_and_avoc',
            'human_and_avoc_perc',
            'human_and_mrc_2_sec_and_complete',
            'human_and_mrc_2_sec_and_complete_perc',
            'video_full_vis_75_duration_no_cap_inview',
            'video_full_vis_75_duration_no_cap_inview_percent',
            'human_and_dentsu_video_ots',
            'human_and_dentsu_video_ots_perc',
            'human_and_viewable_gm_video',
            'human_and_viewable_gm_video_perc',
            'human_and_viewable_gm_video_15cap_sum',
            'human_and_viewable_gm_video_15cap_perc',
            'human_and_groupm_video_ots_completion',
            'human_and_groupm_video_ots_completion_perc',
            'susp_l_measurable_perc',
            'susp_bot_perc',
            'givt_rate',
            'sivt_rate',
            'susp_bot_browser_perc',
            'susp_bot_susp_browser_perc',
            'susp_bot_data_center_perc',
            'susp_bot_spider_perc',
            'susp_ms_abf_perc',
            'susp_bad_domain_perc',
            'susp_bot_proxy_perc',
            'ad_hidden_perc',
            'susp_bot_geo_perc',
            'susp_old_browser_perc',
            'susp_late_night_perc',
            'susp_top_hour_perc',
            'mm_no_referrer_perc',
            'mm_history_avg',
            'susp_incentivized_perc',
            'in_view_measurable_unfiltered_percent',
            'in_view_measurable_git_percent',
            'in_view_measurable_percent',
            'om_sdk_measurable_rate',
            'swf_img_loads',
            'l_mobile',
            'l_mobile_not_iframe',
            'scroll_measurable_impressions',
            'l_somehow_measurable_unfiltered',
            'l_somehow_measurable_git',
            'measurable_impressions',
            '1_sec_in_view_impressions',
            'strict_or_px_2sec_consec_video_ots_unfiltered',
            'strict_or_px_2sec_consec_video_ots_git',
            'video_2_sec_consecutive_visible_unfiltered_percent',
            'video_2_sec_consecutive_visible_git_percent',
            '2_sec_video_in_view_impressions',
            'inview_3sec_cumulative',
            '5_sec_in_view_impressions',
            'in_vp_meas',
            'in_vp',
            'in_vp_perc',
            'om_sdk_measurable_imps',
            'mm_hostile_iframe_perc',
            '1_sec_video_in_view_percent',
            '2_sec_video_in_view_percent',
            'inview_3sec_cumulative_perc',
            '5_sec_video_in_view_percent',
            'l_full_visibility_measurable',
            'l_full_visibility_ots',
            'l_full_visibility_ots_percent',
            'l_full_visibility_ots_1_sec',
            'l_full_visibility_ots_1_sec_percent',
            'fully_on_screen_3sec_cumulative',
            'fully_on_screen_3sec_cumulative_perc',
            'ad_duration',
            'video_in_view_time',
            'percent_of_airtime_visible',
            'video_exposure_time',
            'average_minute_audience',
            'reached_first_quart_sum',
            'reached_first_quart_percent',
            'reached_second_quart_sum',
            'reached_second_quart_percent',
            'reached_third_quart_sum',
            'reached_third_quart_percent',
            'reached_complete_sum',
            'reached_complete_percent',
            'player_audible_on_first_quart_percent',
            'player_audible_on_second_quart_percent',
            'player_audible_on_third_quart_percent',
            'player_audible_on_complete_percent',
            'player_visible_on_first_quart_percent',
            'player_visible_on_second_quart_percent',
            'player_visible_on_third_quart_percent',
            'player_visible_on_complete_percent',
            'player_audible_on_first_quart_sum',
            'player_audible_on_second_quart_sum',
            'player_audible_on_third_quart_sum',
            'player_audible_on_complete_sum',
            'player_visible_on_first_quart_sum',
            'player_visible_on_second_quart_sum',
            'player_visible_on_third_quart_sum',
            'player_visible_on_complete_sum',
            'player_vis_and_aud_on_start_sum',
            'player_vis_and_aud_on_start_percent',
            'player_vis_and_aud_on_first_quart_sum',
            'ad_vis_and_aud_on_first_quart_percent',
            'player_vis_and_aud_on_second_quart_sum',
            'ad_vis_and_aud_on_second_quart_percent',
            'player_vis_and_aud_on_third_quart_sum',
            'ad_vis_and_aud_on_third_quart_percent',
            'player_vis_and_aud_on_complete_sum',
            'ad_vis_and_aud_on_complete_percent',
            'player_audible_full_vis_half_time_sum',
            'player_audible_full_vis_half_time_percent',
            'mrc_2_sec_and_complete',
            'mrc_2_sec_and_complete_perc',
            'dentsu_video_ots',
            'dentsu_video_ots_perc',
            'viewable_gm_video_15cap_sum',
            'viewable_gm_video_15cap_perc',
            'groupm_video_ots_completion',
            'groupm_video_ots_completion_perc',
            'completion_quality',
            'hovers',
            'hovers_percent',
            'time_to_hover_sum',
            'time_to_hover',
            'passthrough_imps',
            'passthrough_rate',
            'small_player_sum',
            'small_player_percent',
            'below_the_fold_sum',
            'below_the_fold_percent',
            'page_ever_focused_sum',
            'out_of_focus_count',
            'out_of_focus_percent',
            'avg_run_time',
            'avg_real_estate_perc',
            'fifty_pct_onscreen_imps',
            'fifty_pct_onscreen_perc',
            'avg_fifty_pct_onscreen_time',
            'fifty_pct_oncreen_audible_imps',
            'fifty_pct_oncreen_audible_perc',
            'avg_fifty_pct_onscreen_time_sound_on',
            'percent_of_ad_length_on_screen',
            'percent_of_ad_length_on_screen_audible',
            'audible_measurable_perc',
            'audible_imps',
            'audible_perc',
            'avg_audible_time',
            'percent_of_ad_length_audible',
            'video_impact_score_measurable_perc',
            'video_impact_score_avg',
            'session_hijacked_perc']}

    
def moat_req(token,query):  
    auth_header = 'Bearer {}'.format(token)
    resp = requests.get( 'https://api.moat.com/1/stats.json',
                        params=query,
                        headers={'Authorization': auth_header})
    if resp.status_code == 200:
        return resp
    else:
        raise Exception("{} Error".format(resp.resp.status_code))

def build_query(level1Id,brandId,tile_type):
    metrics = moat_metrics[tile_type]        
    START_DATE = 20190512
    END_DATE = START_DATE
    metrics  = metrics + ["level1","level2","Level3"]
    
    query = {
    'metrics': ','.join(metrics),
    'start': START_DATE,
    'end': END_DATE,
    'brandId':brandId, ## this is the tile ID 
    'level1Id':level1Id ## this is the campaign
    }   
    
    return query

def main():
    print("Lets Go Dude")
    query = build_query(22443077,2698,"vid_metrics")
    resp = moat_req(TOKEN,query)
    r = resp.json()
    df = pd.DataFrame(r.get('results').get('details'))
    return df


if __name__ == "__main__":
    main()
