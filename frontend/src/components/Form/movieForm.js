import React from 'react'
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/core/styles';
import Input from '@material-ui/core/Input';
import { useState } from 'react';


const AddActorForm = () => {
    const [movieName, setMovieName] = useState('');
    const [date, setReleaseDate] = useState('');


    const onChangeForMovie = (event) => {
        setMovieName(event.target.value)
    }

    const onChangeForDate = (event) => {
        setReleaseDate(event.target.value)
        console.log(date)
    }


 return (
    <Grid item style={{ backgroundColor: 'yellow' }}>
      <h2>Add A Movie</h2>
    <form  noValidate autoComplete="off">
      <Input placeholder="Movie Name" value={movieName} onChange = {onChangeForMovie} inputProps={{ 'aria-label': 'description' }} />
      <Input type="date" onChange={onChangeForDate} placeholder="release date" inputProps={{ 'aria-label': 'description' }} />
      </form>
    </Grid>
 )
}

export default AddActorForm;