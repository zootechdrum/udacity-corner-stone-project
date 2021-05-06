import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';


const useStyles = makeStyles({
  root: {
    minWidth: 275,
    marginTop:'5px'
  },
  bullet: {
    display: 'inline-block',
    margin: '0 2px',
    transform: 'scale(0.8)',
  },
  title: {
    fontSize: 14,
  },
  pos: {
    marginBottom: 12,
  },
});

export default function SimpleCard({ movieName, deleteBtn, id, dltMve, updtBtn }) {
  const classes = useStyles();



  return (

        <Card key={id} className={classes.root}>
          <CardContent>
            <Typography className={classes.title} color="textSecondary" gutterBottom>
              {movieName}
            </Typography>
            <Typography className={classes.pos} color="textSecondary">
              {deleteBtn && <Button id={id} onClick={dltMve} variant="contained" color="secondary">  Delete a Movie</Button>}
            </Typography>
            <Typography variant="body2" component="p">
              {updtBtn && <Button id={id} variant="contained" color="primary">  Update A Movie</Button>}
              <br />
              {'Release Date :'}
            </Typography>
          </CardContent>
          <CardActions>
            <Button size="small">Learn More</Button>
          </CardActions>
        </Card>

  );
}