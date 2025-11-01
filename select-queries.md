# Person

select ?pname
where {
    ?s a schema:Person;
        schema:name ?personname
}

# Place

select ?plname
where {
    {P} schema:spatial ?pl.
    ?pl schema:name ?plname
}