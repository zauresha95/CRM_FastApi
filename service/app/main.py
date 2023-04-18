from datetime import datetime
from fastapi import FastAPI, Depends, status, Response
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import uvicorn
# import sys, os
# sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from .schema import ClientCabinetSchema, AdminCabinetSchema
from ..db.tables import ClientCabinet, AdminCabinet
from ..db.tables import get_session, Base, engine

# This will create db if it doesn't alreasy exist
Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/{id}")
def get_client_cabinet(id: int, session: Session = Depends(get_session)):
    try:
        item = session.query(ClientCabinet).get(id)  # .all()
        if item:
            return item
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": "Record not found"})
    except:
        session.rollback()
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": ''})


@app.post("/")
def add_client(client: ClientCabinetSchema, response: Response, session: Session = Depends(get_session)):
    try:
        item = ClientCabinet(
            name=client.name,
            surname = client.surname,
            email=client.email,
            phone=client.phone,
            date_of_birth=client.date_of_birth
        )
        session.add(item)
        session.commit()
        session.refresh(item)
        response.status_code = status.HTTP_201_CREATED
        return item
        # return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": "Data is not correct"})
    except IntegrityError:
        session.rollback()
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": 'IntegrityError'})
    except TypeError:
        session.rollback()
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": 'TypeError'})
    except Exception as exc:
        print(exc)


@app.put("/{id}")
def update_client_cabinet(id: int, item: ClientCabinetSchema, response: Response, session: Session = Depends(get_session)):
    try:
        itemObject = session.query(ClientCabinet).get(id)
        if itemObject is not None:
            itemObject.name = item.name
            itemObject.email = item.email
            itemObject.phone = item.phone
            itemObject.updated = datetime.now()

            session.commit()
            response.status_code = status.HTTP_204_NO_CONTENT
            return itemObject
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": "Record not found"})
    except:
        session.rollback()
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": ''})


# @app.patch("/{id}")
# def updatePartItem(id: int, item: ClientSchema, response: Response, session: Session = Depends(get_session)):
#     try:
#         itemObject = session.query(Client).get(id)
#         if not itemObject:
#             return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": ''})
#         item_data = item.dict(exclude_unset=True)
#         for key, value in item_data.items():
#             setattr(itemObject, key, value)
#         itemObject.updated = datetime.now()
#         session.add(itemObject)
#         session.commit()
#         session.refresh(itemObject)
#
#         response.status_code = status.HTTP_204_NO_CONTENT
#         return itemObject
#     except TypeError:  # TODO
#         session.rollback()
#         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": ''})  # TODO


# @app.delete("/{id}")
# def deleteItem(id: int, response: Response, session=Depends(get_session)):
#     try:
#         itemObject = session.query(Client).get(id)
#         if itemObject is not None:
#             itemObject = session.query(client.Client).get(id)
#             session.delete(itemObject)
#             session.commit()
#             session.close()
#             response.status_code = status.HTTP_204_NO_CONTENT
#             return 'Item was deleted'
#         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": "Record not found"})
#     except:
#         session.rollback()
#         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": ''})


def main_f():
    uvicorn.run("service.app.main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == '__main__':
    main_f()
