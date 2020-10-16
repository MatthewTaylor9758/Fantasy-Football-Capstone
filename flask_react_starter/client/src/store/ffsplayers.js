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
}

let team_ffsplayers = JSON.parse(localStorage.getItem('ffsplayers'));
const initialState = team_ffsplayers ? team_ffsplayers : {};
console.log(initialState);

export default function ffsplayers(state=initialState, action) {
  switch (action.type) {
    default:
      return state;
  }
}
