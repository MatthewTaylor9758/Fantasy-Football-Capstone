import Cookies from 'js-cookie';

const SET_USER = 'SET_USER';
const REMOVE_USER = 'REMOVE_USER';
const SIGNUP_USER = 'SIGNUP_USER';

export const setUser = (user) => {
  return {
    type: SET_USER,
    user
  }
}

export const removeUser = (user) => {
  return {
    type: REMOVE_USER,
    user
  }
}

export const signupUser = (user) => {
  return {
    type: SIGNUP_USER,
    user
  }
}

export const login = (username, password) => async dispatch => {
  if (!username || !password) {
    return
  }
  console.log(username, password)
  const csrfToken = Cookies.get('XSRF-TOKEN');
  const res = await fetch('/api/users/', {
    method: 'put',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRF-TOKEN': csrfToken
    },
    body: JSON.stringify({username, password})
  });
  const data = await res.json();
  if (res.ok) {
    console.log(data.user);
    localStorage.setItem('user', JSON.stringify(data.user))
    dispatch(setUser(data.user))
  }
  return res;
}

let user = JSON.parse(localStorage.getItem('user'));
let auth = user;
const initialState = user ? auth : {};
console.log(initialState);

export default function authReducer(state=initialState, action) {
  switch (action.type) {
    case SET_USER:
      return action.user;
    default:
      return state;
  }
}
