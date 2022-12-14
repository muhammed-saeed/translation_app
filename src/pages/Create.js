import React, { useState } from 'react'
import Typography from '@material-ui/core/Typography'
import Button from '@material-ui/core/Button'
import Container from '@material-ui/core/Container'
import KeyboardArrowRightIcon from '@material-ui/icons/KeyboardArrowRight'
import { makeStyles, TextareaAutosize } from '@material-ui/core'
import TextField from '@material-ui/core/TextField'
import Radio from '@material-ui/core/Radio'
import RadioGroup from '@material-ui/core/RadioGroup'
import FormControlLabel from '@material-ui/core/FormControlLabel'
import FormControl from '@material-ui/core/FormControl'
import FormLabel from '@material-ui/core/FormLabel'
import { useHistory } from 'react-router-dom'

const useStyles = makeStyles({
  field: {
    marginTop: 20,
    marginBottom: 20,
    display: 'block'
  }
})

export default function Create() {
  const classes = useStyles()
  const history = useHistory()
  const [title, setTitle] = useState('titlenotneeded')
  const [details, setDetails] = useState('')
  const [titleError, setTitleError] = useState(false)
  const [detailsError, setDetailsError] = useState(false)
  const [category, setCategory] = useState('money')

  const handleSubmit = (e) => {
    e.preventDefault()
    setTitleError(false)
    setDetailsError(false)

    if (title == '') {
      setTitleError(true)
    }
    if (details == '') {
      setDetailsError(true)
    }
    if (title && details) {
      fetch('http://localhost:8000/notes', {
        method: 'POST',
        headers: {"Content-type": "application/json"},
        body: JSON.stringify({ title, details, category })
      }).then(() => history.push('/create'))
    } 
  }

  return (
    <Container size="sm">
      <Typography
        variant="h6" 
        color="textSecondary"
        component="h2"
        gutterBottom
      >
        Please Enter Pidgin Text to be translated into English
      </Typography>
      
      <TextField className={classes.field}
          onChange={(e) => setDetails(e.target.value)}
          label="Please Type the PCM Text Here"
          variant="outlined"
          color="secondary"
          multiline
          rows={4}
          fullWidth
          required
          error={detailsError}
        />

      <form noValidate autoComplete="off" onSubmit={handleSubmit}>
        <TextareaAutosize className={classes.field}
          onChange={(e) => setTitle(e.target.value)}
          label="Translated text" 
          variant="outlined" 
          color="secondary" 
          fullWidth
          
        />
        {/* <Radio value="hello" />
        <Radio value="goodbye" /> */}

        <FormControl className={classes.field}>
          <FormLabel>Note Category</FormLabel>
          <RadioGroup value={category} onChange={(e) => setCategory(e.target.value)}>
            <FormControlLabel value="money" control={<Radio />} label="Ernie" />
            <FormControlLabel value="todos" control={<Radio />} label="Merel" />
            <FormControlLabel value="reminders" control={<Radio />} label="PinJie" />
            <FormControlLabel value="work" control={<Radio />} label="Muhammed" />
          </RadioGroup>
        </FormControl>

        <Button
          type="submit" 
          color="secondary" 
          variant="contained"
          endIcon={<KeyboardArrowRightIcon />}>
          Translate PCM to EN
        </Button>
      </form>

      
    </Container>
  )
}
