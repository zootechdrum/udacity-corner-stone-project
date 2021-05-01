import React, { useEffect, useState } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import jwt_decode from "jwt-decode";
import SimpleCard from "../components/Card/movieCard"
import Grid from '@material-ui/core/Grid';
import AddMovieBtn from '../components/Navbar/Buttons/addMovieBtn'
import AddActorBtn from '../components/Navbar/Buttons/addActorBtn'




const Main = () => {
    const { isAuthenticated } = useAuth0();
    const { getAccessTokenSilently } = useAuth0();

    const [mveBtn, setMveBtn] = useState();
    const [actrBtn, setActrBtn] = useState();
    const [movies, setMovies] = useState([]);
    const [isLogin, setLogIn] = useState([false])
    const [permissions, setPermissions] = useState([])

 
    const deleteMovie = (e) => {
        console.log(e.target.id)
        const id = e.target.id
        const requestOptions = {
          method: 'DELETE',
          headers: { 'Content-Type': 'application/json' },
    
      };
    
        fetch('/movies/'+id, requestOptions) 
        .then(res => console.log(res.json()))
    }

    useEffect(() => {
        const data = async () => {
            setLogIn([isAuthenticated])
                try {
                    const token = await getAccessTokenSilently();
                    const decoded = jwt_decode(token)
                    let response = await fetch('/movies', {
                        headers: {
                            Authorization: `Bearer ${token}`
                        }
                    })
                    const data = await response.json()
                    setMovies(data.movies)
                    setPermissions(decoded.permissions)
                    toRenderButton()
                }
                catch (err) {
                    console.log(`something went wrong ${err}`)
                }
        }
        if(isLogin) {data()}

    },isLogin)

    const toRenderButton = () => {
    if( permissions.indexOf('post:movie') && permissions.indexOf('post:actor')){
        setMveBtn(true)
        setActrBtn(true)
    }
}

    return (
        <div>
            {mveBtn ? <AddMovieBtn />: ''}{actrBtn ? <AddActorBtn />: ''}
            {movies.map(movie => (<SimpleCard movieName={"I will be awesome"} 
            dltMve={deleteMovie} 
            id={movie.id} 
            deleteBtn={'true'} />))}
        </div>

    )
};

export default Main;