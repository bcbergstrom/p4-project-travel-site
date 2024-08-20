import React from "react";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Stack from 'react-bootstrap/Stack';
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';
import InputGroup from 'react-bootstrap/InputGroup';

export default function Showluggage(){
return(
    <div>
    <h1>This is your packed Luggage!</h1>
    <img src ='https://cdn.shopify.com/s/files/1/0763/4793/files/Complete_bundle.jpeg?v=1596460228' class="img-fluid"/>


    <Stack direction="horizontal" gap={3}>
      <Form.Control className="me-auto" placeholder="Adding more..." />
      <InputGroup className="mb-3">
        <DropdownButton
          variant="outline-secondary"
          title="Dropdown"
          id="input-group-dropdown-1"
        >
              <Dropdown.Item href="#">Pants</Dropdown.Item>
          <Dropdown.Item href="#">Shirts</Dropdown.Item>
          <Dropdown.Item href="#">Accessories</Dropdown.Item>
        </DropdownButton>
      </InputGroup>
      <Button variant="secondary">Submit</Button>
      <Button variant="outline-danger">Reset</Button>
    </Stack>
    </div>
)
}
