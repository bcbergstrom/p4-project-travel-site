import React from "react";
import Form from 'react-bootstrap/Form'; 
import Button from 'react-bootstrap/Button';
import { useState } from "react";
//the useStates go like
//set the users trip, location, season, is_winter, price, is_flying, and weight_limit
export default function Trip({user}){
    const [fro, setFro] = useState([]);
    const [loc, setLoc] = useState("");
    const [son, setSon] = useState("");
    const [inter, setInter] = useState(false);
    const [rice, setRice] = useState("");
    const [lying, setLying] = useState(false);
    const [lim, setLim] = useState("");
    
  function handleSubmit(e) {
    e.preventDefault();
    fetch("/api/trip",{
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({location:loc, season:son, is_winter:inter, price:rice, is_flying:lying, weight_limit:lim}),
      }
    )
    .then(r=>{
      if (r.ok) { return r.json()}
      else {throw new Error}
    })
    .then(data=>{
      setFro(data)
    })
    .catch(data=>{
      alert("One of your inputs is invalid")
    })
  }
    return(
        <Form>
          {alert(user)}
            <h1 class='display-1' >Lets plan out your trip!!!</h1>
       <Form.Group className='trips' id='location' onSubmit={handleSubmit}>
       <Form.Label>Enter your destination</Form.Label>
       <Form.Control type="location" placeholder="Location" value={loc} onChange={(e)=>setLoc(e.target.value)}/>
       </Form.Group>
       <Form.Group className='trips' id='season'>
       <Form.Label>Enter the season your destination is having</Form.Label>
       <Form.Control type="season" placeholder="Season" value={son} onChange={(e)=>setSon(e.target.value)}/>
       </Form.Group>
       <Form.Group className='trips' id='price'>
       <Form.Label>Enter your price range</Form.Label>
       <Form.Control type="price" placeholder="Price" value={rice} onChange={(e)=>setRice(e.target.value)}/>
       </Form.Group>
       <Form.Check class='form-check-input'type="switch" id="is_winter" label="Is it Winter there?" value={inter} onChange={(e)=>setInter(e.target.value)}/>
       <Form.Check class='form-check-input'type="switch" id="is_flying" label="Are you wanting to fly?" value={lying} onChange={(e)=>setLying(e.target.value)}/>
       <Form.Group className='trips' id='weigtht_limit'>
       <Form.Label>What is the limit of how much your luggage can weigh?</Form.Label>
       <Form.Control type="" placeholder="Luggage weigh" value={lim} onChange={(e)=>setLim(e.target.value)}/>
       </Form.Group>
       <Button type ="submit">Submit</Button>
        </Form>
    )
}