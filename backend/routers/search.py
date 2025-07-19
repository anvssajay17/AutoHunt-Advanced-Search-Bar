from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/search/")
def search_word(q: str = Query(..., min_length=1), db: Session = Depends(get_db)):
   
    q_metaphone = db.execute(text("SELECT dmetaphone(:q)"), {"q": q}).scalar()

    
    query = text("""
        SELECT
            name,
            (
                CASE
                    WHEN position(:q in name) > 0 AND length(:q) >= length(name) * 0.5 THEN 60
                    ELSE 0
                END +
                CASE
                    WHEN name % :q THEN similarity(name, :q) * 30
                    ELSE 0
                END +
                CASE
                    WHEN metaphone = :phonetic THEN 10
                    ELSE 0
                END
            ) AS score
        FROM books
        WHERE
            (position(:q in name) > 0 AND length(:q) >= length(name) * 0.5)
            OR name % :q
            OR metaphone = :phonetic
        ORDER BY score DESC
        LIMIT 20;
    """)

    results = db.execute(query, {"q": q, "phonetic": q_metaphone}).fetchall()

    
    top_result = results[0][0] if results else None

    return {
        "query": q,
        "result": top_result
    }
