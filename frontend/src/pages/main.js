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

    const [mveBtn, setMveBtn] = useState(false);
    const [actrBtn, setActrBtn] = useState(false);
    const [movies, setMovies] = useState([]);
    const [isLogin, setLogIn] = useState([false])
    const [permissions, setPermissions] = useState([])
    const [dltBtn, setDltbtn] = useState()
    const [updtBtn, setUpdtBtn] = useState()




    const deleteMovie = async (e) => {
        const id = e.target.parentElement.id
        const token = await getAccessTokenSilently();
        console.log(token)

        let delRequest = await fetch('/movies/' + id, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                Authorization: `Bearer ${token}`
            },

        })
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
            setPermissions(decoded.permissions, () => console.log("Hello"))
        }
        catch (err) {
            console.log(`something went wrong ${err}`)
        }
    }
    if (isLogin) {
        data()
    }

}, isLogin, permissions)

useEffect(() => {
    toRenderButtons()
})

const toRenderButtons = () => {

    if (permissions.length !== 0) {
        console.log(permissions)

        setMveBtn(true)
        setActrBtn(true)
        setUpdtBtn(true)
        setDltbtn(true)
    }
}
return (
    <div>
        {mveBtn ? <AddMovieBtn /> : ''}{actrBtn ? <AddActorBtn /> : ''}
        {movies.map(movie => (<SimpleCard movieName={movie.title}
            dltMve={deleteMovie}
            id={movie.id}
            deleteBtn={dltBtn}
            updtBtn={true}
        />))}
    </div>

)
};

export default Main;