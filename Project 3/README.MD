# Project 3 - AI Recommendation Logic

## DecodeLabs - Personalization Phase

### Project Goal

Create a simple recommendation system based on user preferences.

## Project Description

This project demonstrates a basic content-based recommendation system.

The system asks the user for their preferred:

- Genre
- Language
- Mood

The user's preferences are then compared with the attributes of different movies.

Each matching preference contributes to a similarity score. The movies are then ranked according to their scores.

## Recommendation Logic

| Preference | Weight |
|------------|--------|
| Genre      | 40%    |
| Language   | 30%    |
| Mood       | 30%    |
| Total      | 100%   |

The movie with the highest similarity score becomes the top recommendation.

## Key Skills

- Logic building
- Pattern matching
- User input
- Similarity scoring
- Recommendation concepts
- Data handling
- Ranking results

## Technologies

- Python

## How to Run

Run:

```bash
python recommendation.py
