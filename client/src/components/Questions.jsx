import React from "react";
import { useState } from "react";
import MenuDropdown from "./Dropdown";
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';

 export default function Allquestions(){

    const [allquest, setallquest]= useState([])
    return(
        <div>
                <Form>
        <h1>Lets get started by packing your luggage!</h1>
            <Container>
                <Row>
                    <Col xs='auto'>Short</Col>
                    <Col>Long</Col>
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
                </Row>
            </Container>
                </Form>
            </div>
    )
}
