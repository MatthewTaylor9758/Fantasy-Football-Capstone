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
  console.log(csrfToken);
  const res = await fetch('/api/users/', {
    method: 'put',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRF-TOKEN': csrfToken
    },
    body: JSON.stringify({username, password})
  });
  const data = await res.json();
  console.log(data);
  if (res.ok && data.user) {
    console.log(data.user);
    localStorage.setItem('user', JSON.stringify(data.user))
    dispatch(setUser(data.user))
  } else {
    return data.errors;
  }
  return data;
}

export const signup = (username, email, password) => async dispatch => {
  const csrfToken = Cookies.get('XSRF-TOKEN')
  console.log(username, email, password)
  const res = await fetch('/api/users/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRF-TOKEN': csrfToken
    },
    body: JSON.stringify({username, email, password})
  });
  const data = await res.json();
  console.log(data);
  if (res.ok && data.user) {
    localStorage.setItem('user', JSON.stringify(data.user));
    dispatch(setUser(data.user))
    return data
  } else {
    return data.errors;
  }
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
