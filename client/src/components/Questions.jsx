import React from "react";
import { useState } from "react";
import MenuDropdown from "./Dropdown";
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
// import Showluggage from "./Luggage";

//the sets go, style shirt, pant, accessorie, is_summer, pants, shirt, and other clothes
 export default function Allquestions(){
    const [allquest, setAllquest]= useState([]);
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
        setAllquest(data)
      })
      .catch(data=>{
        alert("One of your inputs is invalid")
      })
    }
    return(
        <div>
                <Form onSubmit={()=>handleSubmit()}>
        <h1 class='display-1'>Lets get started by packing your luggage!</h1>
            <Container>
                <Row>
                    <Col xs='auto'>Short</Col>
                    <Col>Long</Col>
                    </Row>
                </Container>
                    {/* might have to seperate them all to get better results for the luggage */}
                {['Shirt  ', 'Pants  '].map((type) => (
        <div key={`inline-${type}`} className="mb-3">
        <label for="styles" style={{paddingRight: '10px'}}>{type}</label>
          <Form.Check inline name="style_shirts" type='radio' id='style_shirts' value={sts} onChange={(e)=>setSts(e.target.value)}/>
          <Form.Check inline name="style_pants" type='radio' id='style_pants' value={stp} onChange={(e)=>setStp(e.target.value)}/>
        </div>
      ))}
    <Form.Check type="switch" id="style_accessories" label="Are you an accessories person?" value={sta} onChange={(e)=>setSta(e.target.value)}/>
      <Form.Check type="switch" id="is_Summer" label="Is it summer?"value={mer} onChange={(e)=>setMer(e.target.value)}/>
      <span class= 'input-one-number' id='pants'>Pants</span>
      <input type='integer' className='form-control'value={pan} onChange={(e)=>setPan(e.target.value)}/>
      <span class= 'input-one-number' id='shirts'>Shirts</span>
      <input type='integer' className='form-control'value={ts} onChange={(e)=>setTs(e.target.value)}/>
      <span class= 'input-one-number' id='other_clothes'>Other Clothes</span>
      <input type='integer' className='form-control'value={oc} onChange={(e)=>setOc(e.target.value)}/>
            <MenuDropdown/>
            <Button type ="submit">Submit</Button>
                </Form>
                {/* <Showluggage allquest={allquest} setAllquest={setAllquest}/> */}
            </div>
    )
}
