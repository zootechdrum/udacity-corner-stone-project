import React from 'react'
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/core/styles';
import Input from '@material-ui/core/Input';
import { useState } from 'react';
import Button from '@material-ui/core/Button';
import { useAuth0 } from "@auth0/auth0-react";
import jwt_decode from "jwt-decode";



const AddAMovieForm = () => {
    const [movieName, setMovieName] = useState('');
    const [date, setReleaseDate] = useState('');

    const { isAuthenticated } = useAuth0();
    const { getAccessTokenSilently } = useAuth0();

    

 
    const onChangeForMovie = (event) => {
        setMovieName(event.target.value)
    }

    const onChangeForDate = (event) => {
        setReleaseDate(event.target.value)
    }

    const submit = async() => {
      const token = await getAccessTokenSilently();
      const requestOptions = {
        method: 'POST',
        headers: {
           'Content-Type': 'application/json',
           Authorization: `Bearer ${token}`
          
          },
        body: JSON.stringify({ title: movieName, release_date: date })
    };

      fetch('/add_movie', requestOptions) 
      .then(res => console.log(res.json()))
  }


 return (
    <Grid item style={{ backgroundColor: 'yellow' }}>
      <h2>Add A Movie</h2>
    <form  noValidate autoComplete="off">
      <Input placeholder="Movie Name" value={movieName} onChange = {onChangeForMovie} inputProps={{ 'aria-label': 'description' }} />
      <Input type="date" onChange={onChangeForDate} placeholder="release date" inputProps={{ 'aria-label': 'description' }} />
      </form>
      <Button variant="contained" onClick={submit} color="secondary">
  Add a Movie
</Button>
    </Grid>
 )
}

export default AddAMovieForm;