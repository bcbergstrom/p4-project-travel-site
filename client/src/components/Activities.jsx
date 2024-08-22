import React from "react";
import { useState } from "react";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import InputGroup from 'react-bootstrap/InputGroup';

export default function Places(){
    const [cale, setCale] =useState('')
    const [budget, setBudget] = useState('')
    const [alone, setAlone]= useState(false)
    return(
        <Form>
        <div>
        <h1>Lets get your schedule ready for your trip!!</h1>
        <Form.Label>How much of an adventure are you?</Form.Label>
        <select name='adv' id='adv-scale'>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
        <option value="6">6</option>
        <option value="7">7</option>
        <option value="8">8</option>
        <option value="9">9</option>
        <option value="10">10</option>
        </select>
        <InputGroup size='s'>
        <InputGroup.Text>What is your budget for each activity?</InputGroup.Text>
        <InputGroup.Text>$</InputGroup.Text>
        <Form.Control value={pan} onChange={(e)=>setPan(e.target.value)} aria-label="Amount (to the nearest dollar)" />
        <InputGroup.Text>.00</InputGroup.Text>
      </InputGroup>
        </div>
        </Form>
    )
}