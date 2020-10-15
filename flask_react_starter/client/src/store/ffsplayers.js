import Cookies from 'js-cookie';

const GET_FFSPLAYERS = 'GET_FFSPLAYERS';
const REMOVE_FFSPLAYER = 'REMOVE_FFSPLAYER';
const ADD_FFSPLAYER = 'ADD_FFSPLAYER';



let team_ffsplayers = JSON.parse(localStorage.getItem('ffsplayers'));
const initialState = team_ffsplayers ? team_ffsplayers : {};
console.log(initialState);

export default function ffsplayers(state=initialState, action) {
  switch (action.type) {
    default:
      return state;
  }
}
