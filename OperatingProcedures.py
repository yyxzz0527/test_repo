__author__ = 'daibing'

import pyodbc
import time


class OperatingProcedures:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    @staticmethod
    def _connect_database(connect_str):
        """
        Connect to databases through the param 'connect_str'.
        :param connect_str: The database connection string
        :return: Object of connector
        """
        try:
            connected = pyodbc.connect(connect_str)
            return connected
        except Exception as e:
            print("db connect fail: ", e)

    @staticmethod
    def _capture_cursor(connect_instant):
        """
        Create cursor object, which is typically used to manage the context of a fetch operation.
        :param connect_instant: Instant of connector
        :return: Object of cursor
        """
        try:
            cursor = connect_instant.cursor()
            return cursor
        except Exception as e:
            print("the cursor create error: ", e)

    def execute_procedure(self, connect_str, procedures_name, *args):
        """
        execute procedures(name),then resolve pyodbc's return value
        :param connect_str: connection string
        :param procedures_name: procedures name
        :param args: support multi parameters for procedures(name)
        :return: a txt file, which is conclude the resolved value
        """
        connect_obj = self._connect_database(connect_str)
        cursor_obj = self._capture_cursor(connect_obj)

        args_count = len(*args) - 1
        param_str = '?,' * args_count

        command = "{CALL %s (%s?)}" % (procedures_name, param_str)
        command = command.replace('"', "")
        # print(command)

        cursor_obj.execute(command, *args)
        procedures_content = cursor_obj.fetchall()
        cursor_obj.close()
        connect_obj.close()
        print(procedures_content)
        return procedures_content

    def execute_procedure_no_param(self, connect_str, procedures_name):
        """
        execute procedures(name),then resolve pyodbc's return value
        :param connect_str: connection string
        :param procedures_name: procedures name
        :return: resolved value, which is after execute procedure
        """
        connect_obj = self._connect_database(connect_str)
        cursor_obj = self._capture_cursor(connect_obj)

        command = "{CALL %s}" % procedures_name
        command = command.replace('"', "")

        cursor_obj.execute(command)

        procedures_content = cursor_obj.fetchall()
        print(procedures_content)

        cursor_obj.close()
        connect_obj.close()

    def write_to_file(self, contents):
        """
        write the result (by function "execute procedure") to file(txt,mode is add to file)
        :param contents: the result through function "execute procedure"
        :return: none
        """
        procedures_content = contents
        for row in procedures_content:
            time_path = time.strftime("%Y%m%d%H%M%S", time.localtime())
            try:
                with open('d:/Path/file_' + time_path + '.txt', mode='a+') as fw:
                    fw.write(str(row)+',')
                    fw.close()
            except IOError as e:
                print("operate file error :", e)

    def write_to_database(self,contents):
        """
        write the result (by function "execute procedure") to database(mysql,sql...)
        :return: none
        """
        procedures_content = contents


if __name__ == '__main__':
    op = OperatingProcedures()
    connection_string = 'DRIVER={MySQL ODBC 8.0 ANSI Driver};SERVER=127.0.0.1;DATABASE=db_demo;UID=root;PWD=123456'
    # conn_stat = op._connect_database(connect_str=connection_string)
    # conn_cursor = op._capture_cursor(conn_stat)
    # op.execute_procedure_no_param(connection_string, "proc_no_param")
    # op.execute_procedure(connection_string, "proc_param", (2, "", ""))
    op.write_to_file(op.execute_procedure(connection_string, "proc_param", (2, "", "")))
