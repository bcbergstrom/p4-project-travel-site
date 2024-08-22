import React from "react";
import { useState } from "react";
import MenuDropdown from "./Dropdown";
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import { useNavigate } from "react-router-dom";


//the sets go, style shirt, pant, accessorie, is_summer, pants, shirt, and other clothes

 export default function Allquestions({user, navigate}) {
    const [allquest, setallquest]= useState([]);

    const [sts, setSts] =useState(false);
    const [stp, setStp] = useState(false);
    const [sta, setSta] =useState(false);
    const [mer, setMer] =useState(false);
    const [pan, setPan] =useState("");
    const [ts, setTs] =useState("");
    const [oc, setOc] =useState("");

    function handleSubmit(e) {
      e.preventDefault();
      fetch("/api/luggage",{
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({style_shirt:sts, style_pants:stp, style_accessories:sta, is_summer:mer, pants:pan, shirts:ts, other_clothes:oc}),
        }
      )
      .then(r=>{
        if (r.ok) { return r.json()}
        else {throw new Error}
      })
      .then(data=>{
        setallquest(data)
        navigate('/trip')
      })
      .catch(data=>{
        alert("One of your inputs is invalid")
      })
    }
    
    return(
        <div>
          {/* <body style="background-color:powderblue;"/> */}
                <Form onSubmit={()=>handleSubmit()}>
                  

        <h1 class='display-1'>Lets get started by packing your luggage!</h1>
        <Form.Label>Shirt options</Form.Label>
        <Form.Check type="switch" id="style_shirts" label="Long sleeve or short sleeve?" value={sts} onChange={(e)=>setSts(e.target.value)}/>
        <Form.Label>Pant options</Form.Label>
          <Form.Check type="switch" id="style_pants" label="Pants or shorts?" value={stp} onChange={(e)=>setStp(e.target.value)}/>
    <Form.Check type="switch" id="style_accessories" label="Are you an accessories person?" value={sta} onChange={(e)=>setSta(e.target.value)}/>
      <Form.Check type="switch" id="is_Summer" label="Is it summer?"value={mer} onChange={(e)=>setMer(e.target.value)}/>
      <span class= 'input-one-number' id='pants'>How many pants do you want to pack?</span>
      <input type='integer' className='form-control'value={pan} onChange={(e)=>setPan(e.target.value)}/>
      <span class= 'input-one-number' id='shirts'>How many shirts do you want to pack?</span>
      <input type='integer' className='form-control'value={ts} onChange={(e)=>setTs(e.target.value)}/>
      <span class= 'input-one-number' id='other_clothes'>How many other clothes do you want to pack(socks,underwear,boxers,bra)?</span>
      <input type='integer' className='form-control'value={oc} onChange={(e)=>setOc(e.target.value)}/>
      <Form.Label>How mch of a stress packer are you?</Form.Label>
            <MenuDropdown/>
            <Button type ="submit"class="btn btn-primary btn-sm">Submit</Button>
                </Form>
            </div>
            
    )
}
