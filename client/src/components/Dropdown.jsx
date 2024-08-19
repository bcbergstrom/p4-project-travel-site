import {Dropdown} from 'react-bootstrap'

export default function MenuDropdown(){
    return (
    <Dropdown>
        <Dropdown.Toggle id="dropdown-basic-button">
            How many jeans would you like?
        </Dropdown.Toggle>
        <Dropdown.Menu>
            <Dropdown.Item>1</Dropdown.Item>
            <Dropdown.Item>2</Dropdown.Item>
            <Dropdown.Item>3</Dropdown.Item>
            <Dropdown.Item>4</Dropdown.Item>
            <Dropdown.Item>5</Dropdown.Item>
            <Dropdown.Item>6</Dropdown.Item>
            <Dropdown.Item>7</Dropdown.Item>
            <Dropdown.Item>8</Dropdown.Item>
            <Dropdown.Item>9</Dropdown.Item>
            <Dropdown.Item>10+</Dropdown.Item>
        </Dropdown.Menu>
        </Dropdown>
        
    )
}