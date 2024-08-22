import React from "react";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Stack from 'react-bootstrap/Stack';
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';
import InputGroup from 'react-bootstrap/InputGroup';

export default function Showluggage({allquest, setAllquest}){

  function handleEdit(){
    fetch(`api/`,{
      method:"PATCH",
      headers:{
        "Content-Type": "Application/json"
      },
      body: JSON.stringify({
        pants:Pants,
        shirts:Shirts,
        other_clothes:Other_Clothes
      })
    })
    .then(r=>r.json())
    .then(updatedLug=>{
      const newArr = projects.map(project => {
        if(project.id === updatedProject.id){
          return updatedProject
        }
        return project
      })
      setProjects(newArr)
    })
  }
return(
    <div>
    <h1>This is your packed Luggage!</h1>
    <img src ='https://cdn.shopify.com/s/files/1/0763/4793/files/Complete_bundle.jpeg?v=1596460228' class="img-fluid"/>


    <Stack direction="horizontal" gap={3}>
      <Form.Control className="me-auto" placeholder="Adding more..." />
      <select name='adv' id='adv-scale'>
        <option value="pants">Pants</option>
        <option value="shirts">Shirts</option>
        <option value="other-clothes">Other Clothes</option>
        </select>
      <Button variant="secondary">Submit</Button>
      <Button variant="outline-danger">Reset</Button>
    </Stack>
    <ul>
        <li>Pants-{}</li>
        <li>Shirts-{}</li>
        <li>Other Clothes-{}</li>
    </ul>
    </div>
)
}
