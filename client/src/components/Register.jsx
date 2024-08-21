import Form from 'react-bootstrap/Form';
import button from 'react-bootstrap/Button';
import Button from 'react-bootstrap/Button';
import { Card, Col, Row } from 'react-bootstrap';
import { Navigate, useNavigate } from 'react-router-dom';


function Register() {
    const nav = useNavigate()

    return (
        <div>
            <Row>
                <Col></Col>
                <Col>
                    <h1 className='mt-5 mb-5 text-center'>Traveler</h1>
                    <Form onSubmit={(e) => {
                        e.preventDefault()
                        fetch('/api/users', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({
                                email: e.target[0].value,
                                username: e.target[1].value,
                                budget: Number(e.target[2].value),
                                password: e.target[3].value,
                                is_alone: e.target[4].value == "on" ? true : false
                            })
                        })
                            .then(r => r.json())
                            .then(data => {
                                if (data.errors == null) {
                                    alert("Registration Successful")
                                    nav('/')
                                } else {
                                    alert(data.errors)
                                }
                    })
                            
                    }}>
                        <Form.Group className='mb-3 mt-5' controlId='regEmail'>
                            <Form.Label>Email address</Form.Label>
                            <Form.Control type='email' placeholder='Enter email' />
                            <Form.Text className='text-muted'>
                                Enter your new unique email address
                            </Form.Text>
                        </Form.Group>
                        <Form.Group className='mb-3' controlId='regUsername'>
                            <Form.Label>Username</Form.Label>
                            <Form.Control type='text' placeholder='Enter Username' />
                            <Form.Text className='text-muted'>
                                Enter your new unique username
                            </Form.Text>
                        </Form.Group>
                        <Form.Group className='mb-3' controlId='regBudget'>
                            <Form.Label>Budget</Form.Label>
                            <Form.Control type='number' placeholder='Enter Budget' />
                            <Form.Text className='text-muted'>
                                Enter your new budget in dollars
                            </Form.Text>
                        </Form.Group>
                        <Form.Group className='mb-3' controlId='regPassword'>
                            <Form.Label>Password</Form.Label>
                            <Form.Control type='password' placeholder='Enter Password' />
                            <Form.Text className='text-muted'>
                                Enter your new password
                            </Form.Text>
                        </Form.Group>
                        <Form.Group>
                            <Form.Check
                                type='checkbox'
                                id='is_alone'
                                label='Are you traveling alone?'
                            />
                        </Form.Group>
                        <Button variant='primary' type='submit'  >Register New User</Button>
                    </Form>
                </Col>
                <Col></Col>
            </Row>
        </div>
    )
}

export default Register