import Cookies from 'js-cookie';
import { getLeague } from './leagues';


const GET_TEAM = 'GET_TEAM';
const REMOVE_TEAM = 'REMOVE_TEAM';
const ADD_TEAM = 'ADD_TEAM';

export const grabTeam = (team) => {
  return {
    type: GET_TEAM,
    team
  }
}

export const removeTeam = (team) => {
  return {
    type: REMOVE_TEAM,
    team
  }
}

export const addTeam = (team) => {
  return {
    type: ADD_TEAM,
    team
  }
}

export const getTeam = (ownerId) => async dispatch => {
  const csrfToken = Cookies.get('XSRF-TOKEN');
  console.log(ownerId)
  const response = await fetch(`/api/teams/${ownerId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      // 'X-CSRF-TOKEN': csrfToken
    },
    body: JSON.stringify({ownerId})
  })
  const data = await response.json();
  console.log(data);
  if (response.ok && data.team) {
    localStorage.setItem('team', JSON.stringify(data.team));
    dispatch(grabTeam(data.team));
    dispatch(getLeague(data.team.league_id, data.team.id))
    return data;
  }
  return data;
}

let team = JSON.parse(localStorage.getItem('team'));
const initialState = team ? team : {};
console.log(initialState);

export default function teams(state=initialState, action) {
  switch (action.type) {
    case GET_TEAM:
      return action.team;
    default:
      return state;
  }
}
