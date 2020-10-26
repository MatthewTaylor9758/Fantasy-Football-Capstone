import Cookies from 'js-cookie';

const GET_FFSPLAYERS = 'GET_FFSPLAYERS';
const REMOVE_FFSPLAYER = 'REMOVE_FFSPLAYER';
const ADD_FFSPLAYER = 'ADD_FFSPLAYER';

export const grab_ffsplayer = (ffsplayer) => {
  return {
    type: GET_FFSPLAYERS,
    ffsplayer
  }
}

export const removeffsplayer = (ffsplayer) => {
  return {
    type: REMOVE_FFSPLAYER,
    ffsplayer
  }
}

export const addffsplayer = (ffsplayer) => {
  return {
    type: ADD_FFSPLAYER,
    ffsplayer
  }
}

export const get_ffsplayer = (league_id, team_id) => async dispatch => {
  const res = await fetch(`/api/ffsplayers/${league_id}/${team_id}`);
  const data = await res.json();
  console.log(data);
  if (res.ok && !data.errors) {
    localStorage.setItem('team_players', JSON.stringify(data))
    dispatch(grab_ffsplayer(data))
    return data;
  }
  return data;
}

export const new_ffsplayer = (player_id, league_id, team_id) => async dispatch => {
  const res = await fetch('/api/ffsplayers/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({player_id, league_id, team_id})
  });
  const data = await res.json();
  console.log(data)
  if (res.ok) {
    console.log('somthing')
    const data2 = await dispatch(get_ffsplayer(league_id, team_id))
    console.log(data2)
  }
}

let team_ffsplayers = JSON.parse(localStorage.getItem('team_players'));
const initialState = team_ffsplayers ? team_ffsplayers : {};
console.log(initialState);

export default function ffsplayers(state=initialState, action) {
  switch (action.type) {
    case GET_FFSPLAYERS:
      return action.ffsplayer;
    case ADD_FFSPLAYER:
      return action.ffsplayer;
    default:
      return state;
  }
}
