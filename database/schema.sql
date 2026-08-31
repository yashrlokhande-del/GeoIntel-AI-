CREATE TABLE IF NOT EXISTS countries (
    id SERIAL PRIMARY KEY,
    iso_code VARCHAR(3) UNIQUE,
    name VARCHAR(120) UNIQUE NOT NULL,
    region VARCHAR(120),
    government_type VARCHAR(120),
    population BIGINT,
    gdp_usd NUMERIC
);

CREATE TABLE IF NOT EXISTS sources (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    url TEXT,
    publisher VARCHAR(200),
    publication_date DATE,
    source_type VARCHAR(80),
    reliability_score NUMERIC CHECK (reliability_score >= 0 AND reliability_score <= 1)
);

CREATE TABLE IF NOT EXISTS events (
    id SERIAL PRIMARY KEY,
    event_date DATE NOT NULL,
    country_id INTEGER REFERENCES countries(id),
    event_type VARCHAR(80) NOT NULL,
    severity NUMERIC CHECK (severity >= 0 AND severity <= 100),
    direction VARCHAR(30),
    latitude NUMERIC,
    longitude NUMERIC,
    description TEXT,
    source_id INTEGER REFERENCES sources(id)
);

CREATE TABLE IF NOT EXISTS relationships (
    id SERIAL PRIMARY KEY,
    actor_a INTEGER REFERENCES countries(id),
    actor_b INTEGER REFERENCES countries(id),
    relationship_type VARCHAR(100) NOT NULL,
    strength NUMERIC CHECK (strength >= -1 AND strength <= 1),
    confidence NUMERIC CHECK (confidence >= 0 AND confidence <= 1),
    start_date DATE,
    end_date DATE,
    source_id INTEGER REFERENCES sources(id)
);

CREATE TABLE IF NOT EXISTS country_indicators (
    id SERIAL PRIMARY KEY,
    country_id INTEGER REFERENCES countries(id),
    indicator VARCHAR(160) NOT NULL,
    year INTEGER NOT NULL,
    value NUMERIC,
    source_id INTEGER REFERENCES sources(id)
);

CREATE TABLE IF NOT EXISTS risk_scores (
    id SERIAL PRIMARY KEY,
    country_a INTEGER REFERENCES countries(id),
    country_b INTEGER REFERENCES countries(id),
    score_date DATE NOT NULL,
    security NUMERIC,
    political NUMERIC,
    diplomatic NUMERIC,
    economic NUMERIC,
    social NUMERIC,
    strategic NUMERIC,
    overall NUMERIC,
    confidence NUMERIC
);

CREATE TABLE IF NOT EXISTS scenarios (
    id SERIAL PRIMARY KEY,
    risk_score_id INTEGER REFERENCES risk_scores(id),
    name VARCHAR(160) NOT NULL,
    probability NUMERIC CHECK (probability >= 0 AND probability <= 100),
    impact NUMERIC CHECK (impact >= 0 AND impact <= 100),
    description TEXT
);
