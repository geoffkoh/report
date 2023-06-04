""" 
Summary
=======

A Report is a collection of 

"""

# Standard imports
from dataclasses import dataclass, field
from enum import Enum
import logging
from typing import Dict, List

# Third party imports
from bs4 import BeautifulSoup

# Application imports

logger = logging.getLogger(__name__)

class FlowEnum(Enum):
    """ Direction of Flow """
    HORIZONTAL = 'horizontal'
    VERTICAL = 'vertical'


class ElementTypeEnum(Enum):
    """ The type of the element """
    HEADER = 'header'
    TEXT = 'text'
    PLOT = 'plot'
    IMAGE = 'image'
    DATA = 'data'
    URL = 'url'

# end class ElementTypeEnum


@dataclass
class Element:
    """ An individual element of the report """


@dataclass
class Section:
    """ Class representing a section of the report.

    A Section contains a list of Elements, Section, or List of Section.
    The default flow is vertical.

    """

    # Reference to the parent of this section
    _report: 'Report' = field(default=None)

    parent: 'Section' = field(default=None)

    # List of content for this section.
    contents: List[Element, 'Section'] = field(default_factory=list)

    # Dictionary containing the name (tbd)
    references: Dict[str, Element] = field(default_factory=dict)

    # Whether the flow is horizontal or vertical
    # Default is vertical.
    flow: str = field(default=FlowEnum.VERTICAL.value)

    @property
    def report(self):
        return self._report
    
    @report.setter
    def report(self, report: 'Report'):
        if self._report and id(self._report) != id(report):
            logger.info('Removing section %s from report %s', self, self._report)
            self._report.remove_section(section=self)
        self._report = report

    def generate(self):
        """ Generates an HTML template of this an it's content """

# end class Section



class Report:
    """ Class encapsulating the report itself. """

    root: Section = None

    def __init__(self, title: str = None, root: Section = None):
        """ Creates an instance of a report. 
        
        If root is not provide, this constructor will create an empty
        section as the root.
        """

        if root is not None:
            root = Section()
        self.set_root(root=root)

        self.title = title

    # end __init__()

    def set_title(self, title: str, style: str = None) -> None:
        """ Sets the title of the report """

    def set_root(self, root: Section):
        root.parent = self
        self.root = root

    def add_section(self, name: str = None) -> None:
        """ Adds a new section to the report """
        pass

    def remove_section(self, section: Section) -> None:
        """ Removes a section from the report """
        pass

    def get_section(self, name: str) -> None:
        """ Retrieves a section """
        pass

    def generate(self) -> str:
        """ Creates an HTML template which can then be used for other 
        """
        
        content = ''
        if self.title:
            content = f'<h1>{self.title}</h1>'
        if self.root is not None:
            content = f'{content}<table><tr><td>{self.root.generate()}</td></tr></table>'

    def mail_to(self,
                subject: str = None,
                recipients: List[str] = None,
                senders: List[str] = None):
        """ Sends the report email """
        pass
    # end mail_to()
