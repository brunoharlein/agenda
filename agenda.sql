--
-- PostgreSQL database dump
--

-- Dumped from database version 12.1
-- Dumped by pg_dump version 12.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: event; Type: TABLE; Schema: public; Owner: brunoharlein
--

CREATE TABLE public.event (
    event_id integer NOT NULL,
    title character varying(100) NOT NULL,
    description text,
    event_date date NOT NULL,
    event_time time without time zone NOT NULL
);


ALTER TABLE public.event OWNER TO brunoharlein;

--
-- Name: event_event_id_seq; Type: SEQUENCE; Schema: public; Owner: brunoharlein
--

CREATE SEQUENCE public.event_event_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.event_event_id_seq OWNER TO brunoharlein;

--
-- Name: event_event_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: brunoharlein
--

ALTER SEQUENCE public.event_event_id_seq OWNED BY public.event.event_id;


--
-- Name: event event_id; Type: DEFAULT; Schema: public; Owner: brunoharlein
--

ALTER TABLE ONLY public.event ALTER COLUMN event_id SET DEFAULT nextval('public.event_event_id_seq'::regclass);


--
-- Data for Name: event; Type: TABLE DATA; Schema: public; Owner: brunoharlein
--

COPY public.event (event_id, title, description, event_date, event_time) FROM stdin;
1	un nouveau title 	une nouvelle description 	2020-01-29	11:45:00
\.


--
-- Name: event_event_id_seq; Type: SEQUENCE SET; Schema: public; Owner: brunoharlein
--

SELECT pg_catalog.setval('public.event_event_id_seq', 1, true);


--
-- Name: event event_pkey; Type: CONSTRAINT; Schema: public; Owner: brunoharlein
--

ALTER TABLE ONLY public.event
    ADD CONSTRAINT event_pkey PRIMARY KEY (event_id);


--
-- PostgreSQL database dump complete
--

