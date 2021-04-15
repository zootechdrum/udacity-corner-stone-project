import React from 'react'
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/core/styles';
import Input from '@material-ui/core/Input';
import { useState } from 'react';
import Button from '@material-ui/core/Button';



const AddActorForm = () => {
    const [movieName, setMovieName] = useState('');
    const [date, setReleaseDate] = useState('');


    const onChangeForMovie = (event) => {
        setMovieName(event.target.value)
    }

    const onChangeForDate = (event) => {
        setReleaseDate(event.target.value)
    }

    const submit = () => {
      console.log(date)
      console.log(movieName)

      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
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
  Secondary
</Button>
    </Grid>
 )
}

export default AddActorForm;