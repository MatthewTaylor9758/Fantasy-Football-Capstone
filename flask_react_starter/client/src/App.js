import React, { useEffect, useState }from 'react';
import { BrowserRouter, Switch, Route, NavLink } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import LoginPage from './pages/LoginPage';
import { setUser } from './store/auth'
import UserList from './components/UsersList';


function App() {
    // const [loading, setLoading] = useState(true)
    // const dispatch = useDispatch()
    // useEffect(() => {
    //     const loadUser = async () => {
    //         const res = await fetch("/api/users/current_user");
    //         if (res.ok) {
    //             res.data = await res.json(); // current user info
    //             dispatch(setUser(res.data.user))
    //         }
    //         setLoading(false);
    //     }
    //     loadUser();
    // }, [dispatch]);
    const user = localStorage.getItem('user');
    const currentUser = useSelector(state => state.auth);
    console.log(currentUser);
    console.log("____Rendering app_____")
    // if (loading) {
    //     return <p>loading...</p>
    //   }
    return (
        <BrowserRouter>
            <nav>
                <ul>
                    <li><NavLink to="/" activeclass="active">Home</NavLink></li>
                    <li><NavLink to="/users" activeclass="active">Users</NavLink></li>
                    <li><NavLink to='/login'>Login</NavLink></li>
                </ul>
            </nav>
            <Switch>
                <Route exact path="/users" component={UserList}></Route>
                <Route exact path='/login' component={LoginPage}></Route>
                <Route path="/">
                    <h1>My Home Page</h1>
                </Route>
            </Switch>
        </BrowserRouter>
    );
}

export default App;
