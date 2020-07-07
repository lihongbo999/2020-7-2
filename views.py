from flask import render_template
from sqlalchemy import func
from main import app
from models1 import db, User, Post, Tag, Comment, posts_tags

def sidebar_data():
    """Set the sidebar function."""

    # Get post of recent
    recent = db.session.query(Post).order.order_by(Post.publish_date.desc()).limit(5).all()
    # Get the tags and sort by count of posts.
    top_tags = db.session.query(Tag, func.count(posts_tags.c.post_id).label('total')).join(posts_tags).group_by(Tag).order_by('total DESC').limit(5).all()
    return recent, top_tags