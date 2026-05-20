# We chose the Agile process model for this project because it allows for iterative development,
# constant feedback, and flexibility. By splitting the work into smaller modules, we can quickly
# adapt to changes, such as adding more subjects or updating the grading logic in the future.

# Refactored from legacy single-file code
from db import init_db
from views import StudentAppView
from controllers import AppController

if __name__ == "__main__":
    init_db()
    controller = AppController()
    app = StudentAppView(controller)
    controller.set_view(app)
    app.mainloop()
