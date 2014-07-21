import DS from 'vendor/ember-parse-adapter/lib/ember-parse-adapter';

export default DS.ParseModel.extend({
  photo: DS.attr(''),
  event_total: DS.attr(''),
  type_name: DS.attr(''),
  team_name: DS.attr(''),
  selected_by: DS.attr(''),
  total_points: DS.attr(''),
  current_fixture: DS.attr(''),
  next_fixture: DS.attr(''),
  team_code: DS.attr(''),
  team_id: DS.attr(''),
  status: DS.attr(''),
  code: DS.attr(''),
  first_name: DS.attr(''),
  second_name: DS.attr(''),
  web_name: DS.attr(''),
  now_cost: DS.attr(''),
  chance_of_playing_this_round: DS.attr(''),
  chance_of_playing_next_round: DS.attr(''),
  value_form: DS.attr(''),
  value_season: DS.attr(''),
  cost_change_start: DS.attr(''),
  cost_change_event: DS.attr(''),
  cost_change_start_fall: DS.attr(''),
  cost_change_event_fall: DS.attr(''),
  in_dreamteam: DS.attr(''),
  dreamteam_count: DS.attr(''),
  selected_by_percent: DS.attr(''),
  form: DS.attr(''),
  transfers_out: DS.attr(''),
  transfers_in: DS.attr(''),
  transfers_out_event: DS.attr(''),
  transfers_in_event: DS.attr(''),
  event_points: DS.attr(''),
  points_per_game: DS.attr(''),
  ep_this: DS.attr(''),
  ep_next: DS.attr(''),
  special: DS.attr(''),
  minutes: DS.attr(''),
  goals_scored: DS.attr(''),
  assists: DS.attr(''),
  clean_sheets: DS.attr(''),
  goals_conceded: DS.attr(''),
  own_goals: DS.attr(''),
  penalties_saved: DS.attr(''),
  penalties_missed: DS.attr(''),
  yellow_cards: DS.attr(''),
  red_cards: DS.attr(''),
  saves: DS.attr(''),
  bonus: DS.attr(''),
  ea_index: DS.attr(''),
  bps: DS.attr(''),
  element_type: DS.attr(''),
  team: DS.attr(''),
  current_fixture_is_home: DS.attr(''),
  current_fixture_team_id: DS.attr(''),
  created_at: DS.attr(''),
});
