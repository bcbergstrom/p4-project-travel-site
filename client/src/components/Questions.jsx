import React from "react";
import { useState } from "react";
import MenuDropdown from "./Dropdown";
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import { useNavigate } from "react-router-dom";

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
      fetch("/api/start_luggage",{
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({}),
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
        <div>
          <Form>
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
          <Form.Check inline name="Short" type='radio' id='Short' />
          <Form.Check inline name="Long" type='radio' id='Long'/>
        </div>
      ))}
    <Form.Check type="switch" id="style_accessories" label="Are you an accessories person?"/>
      <Form.Check type="switch" id="is_Summer" label="Is it summer?"/>
      <span class= 'input-one-number' id='pants'>Pants</span>
      <input type='integer' className='form-control'/>
      <span class= 'input-one-number' id='shirts'>Shirts</span>
      <input type='integer' className='form-control'/>
      <span class= 'input-one-number' id='other_clothes'>Other Clothes</span>
      <input type='integer' className='form-control'/>
            <MenuDropdown/>
            <Button type ="submit">Submit</Button>
                </Form>
            </div>
    )
}
