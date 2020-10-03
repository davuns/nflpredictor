import scrape

years = range(2000, 2021)


passing_categories = ['player', 'team', 'pos', 'pass_cmp', 'pass_att', 'pass_cmp_perc', 'pass_yds', 
                  'pass_td', 'pass_td_perc', 'pass_int', 'pass_int_perc', 'pass_first_down', 'pass_yds_per_att',
                  'pass_adj_yds_per_att', 'pass_yds_per_cmp', 'pass_yds_per_g', 'pass_rating', 'pass_sacked',
                  'pass_sacked_yds', 'pass_net_yds_per_att', 'pass_adj_net_yds_per_att', 'pass_sacked_perc', 'comebacks',
                  'gwd']

scrimmage_categories = ['player', 'team', 'pos', 'targets', 'rec', 'rec_yds', 'rec_yds_per_rec',
                  'rec_td', 'rec_first_down', 'rec_per_g', 'rec_yds_per_g', 'catch_pct',
                  'rec_yds_per_tgt', 'rush_att', 'rush_yds', 'rush_td', 'rush_first_down',
                  'rush_yds_per_att', 'rush_yds_per_g', 'rush_att_per_g', 'touches',
                  'yds_per_touch', 'yds_from_scrimmage', 'rush_receive_td', 'fumbles']

defense_categories = ['team', 'points', 'total_yards', 'plays_offense', 'yds_per_play_offense',
                  'turnovers', 'fumbles_lost', 'first_down', 'pass_cmp', 'pass_att', 'pass_yds', 
                  'pass_td', 'pass_int', 'pass_net_yds_per_att', 'pass_fd', 'rush_att', 'rush_yds',
                  'rush_td', 'rush_yds_per_att', 'rush_fd', 'penalties', 'penalties_yds', 'pen_fd',
                  'score_pct', 'turnover_pct', 'exp_pts_def_tot']

kicking_categories = ['player', 'team', 'pos', 'fga1', 'fgm1', 'fga2', 'fgm2', 'fga3', 'fgm3', 'fga4', 'fgm4', 'fga5', 'fgm5',
                  'fga', 'fgm', 'fg_perc', 'xpa', 'xpm', 'xp_perc', 'kickoff', 'kickoff_yds', 'kickoff_tb', 'kickoff_tb_pct',
                  'kickoff_yds_avg', 'punt', 'punt_yds', 'punt_yds_per_punt']

for i in years:
    scrape.generate_csv("passing", i, passing_categories)
    scrape.generate_csv("scrimmage", i, scrimmage_categories)
    scrape.generate_csv("opp", i, defense_categories)
    scrape.generate_csv("kicking", i, kicking_categories)