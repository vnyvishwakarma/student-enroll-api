# student_enroll-api Service

## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all students

**Definition**

`GET /students`

**Response**

- `200 OK` on success

```json
[
    {
        "roll_number": "1",
        "name": "Mayank Koli",
        "stream": "Science"
    },
    {
        "roll_number": "2",
        "name": "Pankaj Sharma",
        "stream": "Science"
    }
]
```

### Registering a new student

**Definition**

`POST /students`

**Arguments**

- `"roll_number":string` a globally unique identifier for student
- `"name":string` name of the student
- `"stream":string` Education Background

If a student with the given identifier already exists, the existing record will be overwritten.

**Response**

- `201 Created` on success

```json
{
        "roll_number": "1",
        "name": "Mayank Koli",
        "stream": "Science"
}
```

## Lookup student details

`GET /student/<identifier>`

**Response**

- `404 Not Found` if the student record does not exist
- `200 OK` on success

```json
{
        "roll_number": "1",
        "name": "Mayank Koli",
        "stream": "Science"
}
```

## Delete a student record

**Definition**

`DELETE /students/<identifier>`

**Response**

- `404 Not Found` if the device does not exist
- `204 No Content` on success