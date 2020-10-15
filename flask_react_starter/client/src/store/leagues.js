import Cookies from 'js-cookie';

const GET_LEAGUE = 'GET_LEAGUE';
const REMOVE_LEAGUE = 'REMOVE_LEAGUE';
const ADD_LEAGUE = 'ADD_LEAGUE';

export const grabLeague = (league) => {
  return {
    type: GET_LEAGUE,
    league
  }
}

export const removeLeague = (league) => {
  return {
    type: REMOVE_LEAGUE,
    league
  }
}

export const addLeague = (league) => {
  return {
    type: ADD_LEAGUE,
    league
  }
}

export const getLeague = (leagueId) => async dispatch => {
  const res = await fetch(`/api/leagues/${leagueId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({leagueId})
  })
  const data = await res.json();
  console.log(data);
  if (res.ok && data.league) {
    localStorage.setItem('league', JSON.stringify(data.league));
    dispatch(grabLeague(data.league))
  }
  return data;
}

let league = JSON.parse(localStorage.getItem('league'));
const initialState = league ? league : {};
console.log(initialState);

export default function leagues(state=initialState, action) {
  switch (action.type) {
    case GET_LEAGUE:
      return action.league
    default:
      return state;
  }
}
