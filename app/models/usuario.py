from app.database.database import db

class Usuario(db.Model):
    __tablename__ = "usuario"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre_usuario = db.Column(
        db.String(150),
        nullable=False
    )

    email = db.Column(
        db.String(150),
        nullable=False,
        unique=True
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    avatar = db.Column(
        db.String(255),
        nullable=True,
        default="default.png"
    )

    rol_id = db.Column(
        db.Integer,
        db.ForeignKey("rol.id"),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now()
    )

    rol = db.relationship(
        "Rol",
        back_populates="usuarios"
    )

    albums = db.relationship(
        "Album",
        back_populates="usuario"
    )

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()