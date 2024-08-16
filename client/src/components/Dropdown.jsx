import {Dropdown} from 'react-bootstrap'

export default function MenuDropdown(){
    return (
    <Dropdown>
        <Dropdown.Toggle id="dropdown-basic-button">
            Menu
        </Dropdown.Toggle>
        <Dropdown.Menu>
            <Dropdown.Item href="#">Action</Dropdown.Item>
            <Dropdown.Item href="#">Another action</Dropdown.Item>
            <Dropdown.Item href="#">Something else</Dropdown.Item>
        </Dropdown.Menu>
        </Dropdown>
    )
}