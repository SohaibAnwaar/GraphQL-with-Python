from orator.migrations import Migration


class CreateMyCarsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('my_cars') as table:
            table.increments('id')
            table.string('name')
            table.timestamps()
            
            

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('my_cars')
