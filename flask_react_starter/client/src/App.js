import React, { useEffect, useState }from 'react';
import { BrowserRouter, Switch, Route, NavLink } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import LoginPage from './pages/LoginPage';
import SignupPage from './pages/SignupPage';
import MyTeamPage from './pages/MyTeamPage';
import AvailPlayers from './pages/AvailPlayers';
import SplashPage from './pages/SplashPage';
import { setUser } from './store/auth'
import UserList from './components/UsersList';
import { AuthRoute, ProtectedRoute } from './components/Routes';

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
    const currentUser = useSelector(state => state.auth.id);
    console.log(currentUser);
    console.log("____Rendering app_____")
    return (
        <BrowserRouter>
            <Switch>
                <Route exact path="/users" component={UserList} currentUserId={currentUser}></Route>
                <Route exact path='/login' component={LoginPage} currentUserId={currentUser}></Route>
                <Route exact path='/signup' component={SignupPage} currentUserId={currentUser}></Route>
                <ProtectedRoute path='/myTeam/:id' component={MyTeamPage} currentUserId={currentUser}></ProtectedRoute>
                <ProtectedRoute exact path='/players' component={AvailPlayers} currentUserId={currentUser}></ProtectedRoute>
                <Route path="/" component={SplashPage}></Route>
            </Switch>
        </BrowserRouter>
    );
}

export default App;
