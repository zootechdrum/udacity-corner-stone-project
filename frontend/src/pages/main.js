import React, { useEffect, useState } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import jwt_decode from "jwt-decode";
import SimpleCard from "../components/Card/movieCard"
import ActorCard from "../components/Card/actorCard"
import Grid from '@material-ui/core/Grid';
import AddMovieBtn from '../components/Navbar/Buttons/addMovieBtn'
import AddActorBtn from '../components/Navbar/Buttons/addActorBtn'

import { makeStyles } from '@material-ui/core/styles';
import Modal from '@material-ui/core/Modal';

import Actor from '../API/actorApi'


const useStyles = makeStyles({
    root: {
        background: '#000'
    }
});





const Main = () => {
    const { isAuthenticated } = useAuth0();
    const { getAccessTokenSilently } = useAuth0();

    const [mveBtn, setMveBtn] = useState(false);
    const [actrBtn, setActrBtn] = useState(false);
    const [movies, setMovies] = useState([]);
    const [actors, setActors] = useState([]);
    const [isLogin, setLogIn] = useState([false])
    const [permissions, setPermissions] = useState([])
    const [dltBtn, setDltbtn] = useState()
    const [updtBtn, setUpdtBtn] = useState()
    const [open, setOpen] = useState(false);



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

    const deleteActor = async (e) => {
        const id = e.target.parentElement.id;
        const token = await getAccessTokenSilently();
        Actor.delete(id, token)
    }


    const getActors = async () => {
        setLogIn([isAuthenticated])
        try {
            const token = await getAccessTokenSilently();
            const decoded = jwt_decode(token)
            let response = await fetch('/actors', {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            })
            const data = await response.json()
            console.log(data.actors[0].name)
            setActors(data.actors)
            // setPermissions(decoded.permissions)
        }
        catch (err) {
            console.log(`something went wrong ${err}`)
        }
    }


    const handleOpen = () => {
        console.log('hello')
        setOpen(true);
    };

    const handleClose = () => {
        setOpen(false);
    };



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
            }
            catch (err) {
                console.log(`something went wrong ${err}`)
            }
        }
        if (isLogin) {
            console.log("hell")
            data()
            getActors()
        }

    }, isLogin, permissions, actors)

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
            <Grid container>
                <Grid item className={classes.root} xs={12}>
                    {mveBtn ? <AddMovieBtn /> : ''}{actrBtn ? <AddActorBtn /> : ''}
                </Grid>
                <Grid item xs={6}>

                    {movies.map(movie => (<SimpleCard movieName={movie.title}
                        dltMve={deleteMovie}
                        id={movie.id}
                        deleteBtn={dltBtn}
                        updtBtn={true}
                    />))}
                </Grid>
                <Grid item xs={6}>
                    {actors.map(actor => (<ActorCard actorName={actor.name}
                        dltMve={deleteActor}
                        openMdl={handleOpen}
                        deleteBtn={dltBtn}
                        updtBtn={true}
                        id={actor.id}
                    />))}
                </Grid>
                <Modal
                    open={open}
                    onClose={handleClose}
                    aria-labelledby="simple-modal-title"
                    aria-describedby="simple-modal-description"
                >
                </Modal>
            </Grid>
        </div>

    )
};

export default Main;